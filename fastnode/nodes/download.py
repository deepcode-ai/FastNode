import os
import time
from fastnode.logger.logger import logger
from fastnode.models.files import Files
from fastnode.models.actions import Actions
from fastnode.factories.node_factory import NodeFactory
from fastnode.nodes.click_and_type import ClickableAndTypeableNode
from fastnode.utils.decorators.retry_decorator import retry
from fastnode.utils.screenshot_generator import ScreenshotGenerator


@NodeFactory.register_node_type("download")
class DownloadNode(ClickableAndTypeableNode):

    @retry(max_attempts=3, backoff=5)
    def run(self, steps, history, objective, web_automater, db_session, s3_client, request_id, request_dir, prompt,
            llm_response, loop, previous_node, **kwargs):
        try:
            time.sleep(120)
            self.loop = loop
            self.loop.run_until_complete(web_automater.page.reload())

            logger.info(f"Download Node initiated for request_id: {request_id}."
                        f" It might take 10-15 minutes to complete.")

            self.screenshot_filename, self.screenshot_id = ScreenshotGenerator().run(
                db_session, s3_client, web_automater, steps, request_id, request_dir, self.loop
            )

            cropped_images_folder = os.path.join(request_dir, "cropped_images")
            os.makedirs(cropped_images_folder, exist_ok=True)
            self._get_clicking_location(self.screenshot_filename, cropped_images_folder, previous_node, db_session,
                                        s3_client, web_automater, steps, request_id, request_dir)

            logger.info(f"Clicking to download the output")
            download_file_path = os.path.join(request_dir, f"downloaded_{request_id}.csv")
            self.loop.run_until_complete(
                web_automater.download_on_click(location=self.location, download_path=download_file_path)
            )

            logger.info(f"Downloaded the output to {download_file_path}")

            # Uncomment If you have aws account and want to store result in your AWS S3
            # s3_client.upload_file(file_path=download_file_path)
            Files.add_file(
                session=db_session,
                request_id=request_id,
                path=download_file_path,
                category="OUTPUT",
                file_type="csv",
                meta_data=None,
            )
            self.output = download_file_path
        except Exception as e:
            logger.error(f"Download Node failed. Retrying... {e}")
            raise e

    def actions_taken(self):
        return f"Downloaded the output to {self.output}"

    def update_action_in_db(self, session, request_id, prompt, llm_response):
        Actions.add_action_taken(
            session=session,
            request_id=request_id,
            screenshot_id=None,
            prompt=prompt,
            llm_response=llm_response,
            action=f"Downloaded the output to {self.output}",
            node_id=self.id,
            text="",
        )

    def __repr__(self):
        return f"DownloadNode({self.id}, {self.node_name}, {self.description})"
