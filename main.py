from modules import FinalAPISelector, ArgumentExtractor, SubAPISelector
from retriever import VectorDataBase
from executor import Executor
from result_formatter import ResultFormatter
from configparser import ConfigParser
import os
import json
from collections import deque
import logging

import warnings
warnings.filterwarnings("ignore")

config = ConfigParser()
config.read("config.ini")

DATA_PATH = config["faiss"]["data"]

OPENAI_SECRET_KEY = config["openai"]["secret_key"]
MODEL = config["openai"]["model"]
TEMPERATURE = float(config["openai"]["temperature"])

QUERY = config["query"]["query"]

os.environ["OPENAI_API_KEY"] = OPENAI_SECRET_KEY

if __name__ == "__main__":
    vector_db = VectorDataBase()
    vector_db.load_db()

    api_selector = FinalAPISelector(MODEL, TEMPERATURE)
    argument_extractor = ArgumentExtractor(MODEL, TEMPERATURE)
    sub_api_selector = SubAPISelector(MODEL, TEMPERATURE)
    executor = Executor()
    formatter = ResultFormatter(MODEL, TEMPERATURE)

    logging.basicConfig(
        level=logging.INFO,
        filename="logs/run.log",
        filemode="w",
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logger = logging.getLogger()

    query = QUERY

    logger.info(f"Query : {query}")

    ## getting the root api
    api = api_selector.select_api_from_query(query=query, db=vector_db)
    api = json.loads(api)

    logger.info(f'Final API Output: {api}')

    if api == "None":
            print("[]")
            exit()

    with open(api['data_source'], "r") as f:
            api_documentation = f.read()

    arguments = argument_extractor.get_arguments_from_query(query=query, db=vector_db, api_documentation=api_documentation)
    arguments = json.loads(arguments)
    logger.info(f'Argument for {api["api_name"]}: {arguments}')

    stack = deque()

    for key, value in arguments.items():
        if value is None:
            stack.append(key)

    api_tree = []

    function_json = {"api_name": api["api_name"], "arguments": arguments}

    logger.info(f"JSON: {function_json}")

    response = executor.run(function_json)
    status_code = response.pop("status")
    if status_code != 200:
        execution_response_msg = (
            "Unsuccessful attempt, cause: " + response.get("error", "unknown") + "!"
        )
    else:
        execution_response_msg = response.pop("message")

    api_call_summary = {
        "sequence_no": len(api_tree),
        "api_name": api["api_name"],
        "arguments": arguments,
        "output": response,
    }
    api_tree.append(api_call_summary)

    # if arguments are not found
    while(stack):
        next_required_argument = stack.pop()
        api_tree.append(next_required_argument)

        api = sub_api_selector.get_api_from_argument(required_argument=next_required_argument, db=vector_db)

        api = json.loads(api)

        if api == "None":
            print("[]")
            exit()

        logger.info(f'Final API Output: {api}')

        with open(api['data_source'], "r") as f:
            api_documentation = f.read()

        arguments = argument_extractor.get_arguments_from_query(query=query, db=vector_db, api_documentation=api_documentation)
        arguments = json.loads(arguments)
        logger.info(f'Argument for {api["api_name"]}: {arguments}')

        for key, value in arguments.items():
            if value is None:
                stack.append(key)

        function_json = {"api_name": api["api_name"], "arguments": arguments}

        logger.info(f"JSON: {function_json}")

        response = executor.run(function_json)
        status_code = response.pop("status")
        if status_code != 200:
            execution_response_msg = (
                "Unsuccessful attempt, cause: " + response.get("error", "unknown") + "!"
            )
        else:
            execution_response_msg = response.pop("message")

        api_call_summary = {
            "sequence_no": len(api_tree),
            "api_name": api["api_name"],
            "arguments": arguments,
            "output": response,
        }
        api_tree.append(api_call_summary)

    formatted_result = formatter.run(api_tree)
    
    with open("output/run.json", "w") as f:
        f.write(formatted_result)
        f.close()
