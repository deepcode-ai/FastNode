## FastNode: A Neuro-Graphic Self-Learnable Engine

<p>
<a href="https://twitter.com/_fastAGI" target="blank">
<img src="https://img.shields.io/twitter/follow/_fastAGI?label=Follow: _fastAGI&style=social" alt="Follow _fastAGI"/>
</a>
<a href="https://www.reddit.com/r/Fast_AGI" target="_blank"><img src="https://img.shields.io/twitter/url?label=/r/Fast_AGI&logo=reddit&style=social&url=https://github.com/KhulnaSoft/FastAGI"/></a>

<a href="https://discord.gg/dXbRe5BHJC" target="blank">
<img src="https://img.shields.io/discord/1107593006032355359?label=Join%20FastAGI&logo=discord&style=social" alt="Join FastAGI Discord Community"/>
</a>
<a href="https://www.youtube.com/@_fastagi" target="_blank"><img src="https://img.shields.io/twitter/url?label=Youtube&logo=youtube&style=social&url=https://github.com/KhulnaSoft/FastAGI"/></a>
</p>

<p><b>Share This Repository</b></p>

<p>

<a href="https://x.com/intent/post?text=Check+out+Fastnode+by+FastAGI+%3A+A+Self-Learnable+Engine+for+Cognitive+GUI+Automation+&url=https%3A%2F%2Fgithub.com%2FKhulnaSoft%2FFastNode&hashtags=Fastnode%2CFastAGI%2CAGI" target="blank">
<img src="https://img.shields.io/twitter/follow/_fastAGI?label=Share Repo on Twitter&style=social" alt="Follow _fastAGI"/></a> 
<a href="https://t.me/share/url?text=Check%20out%20FastNode%20by%20FastAGI%20:%20A%20Self-Learnable%20Engine%20for%20Cognitive%20GUI%20Automation%20&url=https://github.com/KhulnaSoft/FastNode" target="_blank"><img src="https://img.shields.io/twitter/url?label=Telegram&logo=Telegram&style=social&url=https://github.com/KhulnaSoft/FastNode" alt="Share on Telegram"/></a>
<a href="https://api.whatsapp.com/send?text=Check%20out%20FastNode%20by%20FastAGI%20-%20A%20Self-Learnable%20Engine%20for%20Cognitive%20GUI%20Automation%20:%20https://github.com/KhulnaSoft/FastNode"><img src="https://img.shields.io/twitter/url?label=whatsapp&logo=whatsapp&style=social&url=https://github.com/KhulnaSoft/FastNode" /></a> <a href="https://www.reddit.com/submit?url=https%3A%2F%2Fgithub.com%2FKhulnaSoft%2FFastNode&title=Check+out+FastNode+by+FastAGI+%3A+A+Self-Learnable+Engine+for+Cognitive+GUI+Automation&type=TEXT" target="blank">
<img src="https://img.shields.io/twitter/url?label=Reddit&logo=Reddit&style=social&url=https://github.com/KhulnaSoft/FastAGI" alt="Share on Reddit"/>
</a> <a href="mailto:?subject=Check%20out%20FastNode%20by%20FastAGI%20-%20A%20Self-Learnable%20Engine%20for%20Cognitive%20GUI%20Automation%20:%20https://github.com/KhulnaSoft/FastNode" target="_blank"><img src="https://img.shields.io/twitter/url?label=Gmail&logo=Gmail&style=social&url=https://github.com/KhulnaSoft/FastNode"/></a>

</p>

<hr>

## What is FastNode?

FastNode is a self-operating computer system designed to automate web interactions and data extraction processes. It leverages advanced technologies like OCR (Optical Character Recognition), YOLO (You Only Look Once) models for object detection, and a custom site-graph to navigate and interact with web pages programmatically.


## Installation

To get started with FastNode, you need to have Python installed on your system. Follow these steps to install FastNode:

1. Open your terminal and clone the FastAGI repository.
```
git clone https://github.com/KhulnaSoft/FastNode.git 
```

2. Navigate to the root of the cloned repository directory using the command:
```
cd FastNode
```
3. Create a copy of .env.example , and name it .env. Repeat this step for all the three modules - fastnode, yolo, ocr

4. Ensure that Docker is installed on your system. You can download and install it from [here](https://docs.docker.com/get-docker/).

5. Once you have Docker Desktop running, run the following command in the FastNode directory:

```
docker compose -f docker-compose.yaml up --build
```

6. Open your web browser and navigate to http://localhost:8001/health to check server is running


## How to Use FastNode

FastNode operates based on a site-graph that defines the navigation and actions to be performed on a website. Here's a basic overview of how to use FastNode:

1. Define Your Objective: Specify what you want to achieve with FastNode, such as data extraction or automation of specific web interactions.


2. Prepare Your Fastnode-Site-Graph: Create a JSON file that represents the site-graph. This graph outlines the nodes (web elements) and edges (actions) that FastNode will navigate and interact with.


3. Prepare you FastNode initiator planner prompt : Using the template structure given for planner prompts in openai_prompts.py, for OpenAI LLM, you can create a new prompt file in the prompts directory with structure <llm_prompts.py> 


4. Run FastNode: 

    ### Using FastNode via API

    FastNode can be controlled and utilized through its API, allowing users to automate web interactions and data extraction tasks programmatically. This guide will walk you through the process of sending requests to FastNode using its API endpoint.

    #### Accessing the API Documentation

    Before you start, ensure that FastNode is running on your local machine. Once FastNode is up and running, you can access the API documentation by visiting:

     ```
    http://localhost:8001/docs
     ```
     This URL will take you to the Swagger UI, where you can find detailed documentation on all available API endpoints, including the one used to initiate FastNode tasks.

     #### Sending a Request to FastNode

     To automate a task with FastNode, you will use the /api/fastnode/initiate endpoint. This endpoint accepts a JSON payload that specifies the task's objective, the path to the site-graph JSON file, the root node to start traversal, and the URL of the website you wish to interact with.

     #### Request Structure
     Here is the structure of the JSON payload you need to send to the `/api/fastnode/initiate` endpoint:

     ```
     {
         "site_url": "string",
         "objective": "string",
         "graph_path": "string",
         "planer_prompt": "string"
     
     }
     ```
     
     Example request:
     {
        "site_url": "https://app.apollo.io/#/login",
        "objective": "Find the list of 20 ceo, cto of tech companies in san francisco. Login into apollo using the creds example@example.com and password dummypassword@123",
        "graph_path": "fastnode/site_trees/apollo.json"
        "planner_prompt": "apollo"
     }
     
     - site_url: The URL of the website FastNode will visit and interact with.

     - objective: The goal you want to achieve on the website. This could be anything from data extraction to automating a series of web interactions. Make sure you provide the login instructions along with the credentials if login is required in your use-case

     - graph_path: The path to the JSON file that contains your site-graph. The site-graph defines the structure and navigation flow of the website for FastNode.

     - planner_prompt: The key for planning prompt. You can change or map new key in planning_agent.py for FastNode planner prompt.


   #### Using CURL

     ```
     curl -X 'POST' \
         'http://localhost:8001/api/fastnode/initiate' \
         -H 'accept: application/json' \
         -H 'Content-Type: application/json' \
         -d '{
         "site_url": "https://example.com/products",
         "objective": "Extract product details",
         "graph_path": "/path/to/your/site-graph.json"
         "planner_prompt": "planner_key"
         
     }'
     ```

## YOLO/OCR Models

FastNode utilizes YOLO models for object detection and OCR for text recognition on web pages. These models are crucial for identifying clickable elements, reading text from images, and interacting with web pages dynamically.

We are providing some general yolo models trained on `YOLO-V8` over thousands of web-screenshots
Navigate to - `yolo/web_detection_models/` dir to find those

### How to Train Your Own YOLO Model

1. Collect a Dataset: Gather images of the web elements you want to detect and annotate them with bounding boxes.

2. Prepare the Dataset: Split your dataset into training and validation sets.

3. Train the Model: Use a YOLO training script to train your model on the prepared dataset. Adjust the training parameters according to your needs.

4. Evaluate the Model: Test your trained model on a separate test set to evaluate its performance.

5. Integrate with FastNode: Once trained, integrate your custom YOLO model with FastNode by specifying the model path in the configuration.

### Hosting Custom YOLO model and OCR apps remotely

If you don't have enough resources on your local machine, you can host the OCR and YOLO modules on any cloud server. Following steps can be taken:

1. In your ocr/.env file, add USE_REMOTE_OCR=True and set the url for the remote service in OCR_REMOTE_URL

2. In your yolo/.env file, add USE_REMOTE_YOLO=True and set the url for the remote service in YOLO_REMOTE_URL

3. Update the yolo web detection model path in your yolo/.env file, add SAHI_MODEL_PATH and ULTRALYTICS_MODEL_PATH. 
Example: SAHI_MODEL_PATH = yolo/web_detection_models/twitter.pt

 

### FastNode-Site-Graph Preparation
The site-graph is a JSON file that describes the structure and navigation flow of a website for FastNode. Here's how to prepare it:

1. Identify Web Elements: Navigate through your target website and identify the key elements you want to interact with, such as buttons, text-boxes, and links.

2. Define Nodes: For each web element, define a node in the JSON file. Include properties like node_name, actionable_element_type, location, and is_type.

3. Define Edges: Specify the relationships between nodes using adjacent_to and adjacent_from properties to represent the navigation flow.

4. Include Action Details: For nodes that require typing or clicking, provide additional details like type_description or click_action.

Example of a simple site-graph:

```
{
    "1": {
        "node_type": "clickable_and_typeable",
        "node_name": "Login Button",
        "actionable_element_type": "button",
        "location": [100, 200],
        "is_type": false,
        "adjacent_to": ["2"]
    },
    "2": {
        "node_type": "clickable_and_typeable",
        "node_name": "Username Field",
        "actionable_element_type": "textbox",
        "location": [150, 250],
        "is_type": true,
        "type_description": "Enter username here",
        "adjacent_to": []
    }
}
```

### Storing Debugging Screenshots & Downloaded Output


Screenshots at every node for web element detection is stored in requests directory in the root folder. You can store them on an AWS s3 account in case you wish to, or persist them locally or neither as per your choice.
For use-cases which require downloading output, downloadable content (like output in apollo) needs to be stored either locally or remotely.

1. Storing Screenshots & Downloads Remotely
 - In your fastnode/.env file, configure AWS keys AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY from your AWS console
 - In fastnode/services/fastnode.py, uncomment the following snippet at line 35, 

 ```
    # Uncomment If you have aws account and want to store result in your AWS S3
    # self.s3_client = S3Helper(access_key=self.config.AWS_ACCESS_KEY_ID,
    #                           secret_key=self.config.AWS_SECRET_ACCESS_KEY,
    #                           bucket_name=self.config.bucket_name)
```
 and pass s3_client=self.s3_client at line 84
 
 ```
    s3_client=None
 ```
 - In fastnode/utils/screenshot_generator.py uncomment this on line 18,

 ```
    # Uncomment If you have aws account and want to store result in your AWS S3
    s3_client.upload_file(file_path=screenshot_filename)
 ```
 - In fastnode/nodes/download.py uncomment this on line 44
 
 ```
    # Uncomment If you have aws account and want to store result in your AWS S3
    s3_client.upload_file(file_path=download_file_path)
 ```

 2. Storing Screenshots & Downloaded files locally
 - By default, the screenshots and downloaded output are stored locally during execution and are deleted as the task completes or fails
 - In fastnode/worker.py comment this finally block on line 79 to persist screenshots locally,
 ```
    finally:
            # Comment if you don't want to delete screenshots locally
            if os.path.exists(screenshots_dir):
                logger.info(f"Deleting request directory {screenshots_dir}")
                shutil.rmtree(screenshots_dir)
            session.close()
 ```
