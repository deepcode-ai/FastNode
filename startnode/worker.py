import os
import shutil
from celery import Celery
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from asgi_correlation_id.extensions.celery import load_correlation_ids
from startnode.logger.logger import logger
from startnode.services.startnode import StartnodeService
from startnode.models.requests import Requests
from startnode.utils.enums.request_status import RequestStatus

load_dotenv()
REDIS_URL = os.getenv("REDIS_URL")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"

# logger = logger.getLogger(__name__)


def connect_db():
    engine = create_engine(
        DB_URL,
        pool_size=20,  # Maximum number of database connections in the pool
        max_overflow=50,  # Maximum number of connections that can be created beyond the pool_size
        pool_timeout=30,  # Timeout value in seconds for acquiring a connection from the pool
        pool_recycle=1800,  # Recycle connections after this number of seconds (optional)
        pool_pre_ping=False,  # Enable connection health checks (optional)
    )
    connection = engine.connect()
    connection.close()
    return engine


celery_app = Celery(
    "worker",
    broker=REDIS_URL,
    backend=REDIS_URL,
    # include=["jobs.test_job"],
    # imports=["worker"],
)


def create_session():
    engine = connect_db()
    session = sessionmaker(bind=engine)()
    return session


load_correlation_ids()


@celery_app.task
def initiate_startnode(
        objective: str,
        screenshots_dir: str,
        url: str,
        graph_path: str,
        request_id: int,
        planner_prompt: str,
        root_node: str = "1",
):
    session = create_session()
    logger.info(f"Initiating Startnode for request {request_id}")
    try:
        driver = StartnodeService(
            objective=objective, graph_path=graph_path, root_node=root_node
        )
        driver.run(session=session, request_id=request_id, url=url, request_dir=screenshots_dir,
                   planner_prompt=planner_prompt)

    except Exception as e:
        Requests.update_request_status(session=session, request_id=request_id, status=RequestStatus.FAILED.value)
        logger.error(f"Error while running startnode for request_id: {request_id}: {str(e)}")

    finally:
        # Comment if you don't want to delete screenshots locally
        if os.path.exists(screenshots_dir):
            logger.info(f"Deleting request directory {screenshots_dir}")
            shutil.rmtree(screenshots_dir)
        session.close()
