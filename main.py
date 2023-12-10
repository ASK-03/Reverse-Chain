from modules import FinalAPISelector, ArgumentExtractor, SubAPISelector
from vector_db import VectorDataBase
from configparser import ConfigParser
import os
import json
from collections import deque

import warnings
warnings.filterwarnings("ignore")

config = ConfigParser()
config.read("config.ini")

DATA_PATH = config["faiss"]["data"]

OPENAI_SECRET_KEY = config["openai"]["secret_key"]
MODEL = config["openai"]["model"]
TEMPERATURE = float(config["openai"]["temperature"])

os.environ["OPENAI_API_KEY"] = OPENAI_SECRET_KEY

if __name__ == "__main__":
    vector_db = VectorDataBase()
    vector_db.load_db()

    query = "Summarize work items similar to don:core:dvrv-us-1:devo/0:issue/1"
    # query = "What is the meaning of life?"
    # query = "Prioritize my P0 issues and add them to the current sprint"
    # query = "List all high severity tickets coming in from slack from customer Cust123 and generate a summary of them"
    # query = "Given a customer meeting transcript T, create action items and add them to my current sprint"


    api_selector = FinalAPISelector(MODEL, TEMPERATURE)
    argument_extractor = ArgumentExtractor(MODEL, TEMPERATURE)
    sub_api_selector = SubAPISelector(MODEL, TEMPERATURE)

    ## getting the root api
    api = api_selector.select_api_from_query(query=query, db=vector_db)
    api = json.loads(api)

    print(api)

    if api == "None":
            print("[]")
            exit()

    with open(api['data_source'], "r") as f:
            api_documentation = f.read()

    arguments = argument_extractor.get_arguments_from_query(query=query, db=vector_db, api_documentation=api_documentation)
    arguments = json.loads(arguments)
    stack = deque()

    print(arguments)
    for key, value in arguments.items():
        if value is None:
            stack.append(key)

    api_tree = []
    api_tree.append(api['api_name'])


    while(stack):
        next_required_argument = stack.pop()
        api_tree.append(next_required_argument)

        api = sub_api_selector.get_api_from_argument(required_argument=next_required_argument, db=vector_db)

        api = json.loads(api)

        if api == "None":
            print("[]")
            exit()

        print(api)

        with open(api['data_source'], "r") as f:
            api_documentation = f.read()

        arguments = argument_extractor.get_arguments_from_query(query=query, db=vector_db, api_documentation=api_documentation)

        arguments = json.loads(arguments)

        for key, value in arguments.items():
            if value is None:
                stack.append(key)
        print("Arguments")
        print(arguments)
    
    print("==== API TREE ====")
    print(api_tree)