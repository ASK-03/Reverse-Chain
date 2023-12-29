from typing import Dict, Any
import server
import json

class Executor:
    def __init__(self):
        pass

    def run(self, function_json) -> Dict[str, Any]:
        function_name = function_json.get("api_name")
        function_args = function_json.get("arguments")

        if function_name == "get_sprint_id":
            return server.get_sprint_id()
        elif function_name == "get_similar_work_items":
            work_id = function_args.get("work_id")
            return server.get_similar_work_items(work_id)
        elif function_name == "add_work_items_to_sprint":
            work_ids = function_args.get("work_ids")
            sprint_id = function_args.get("sprint_id")
            return server.add_work_items_to_sprint(work_ids, sprint_id)
        elif function_name == "create_actionable_tasks_from_text":
            text = function_args.get("text")
            return server.create_actionable_tasks_from_text(text)
        elif function_name == "prioritize_objects":
            objects = function_args.get("objects")
            return server.prioritize_objects(objects)
        elif function_name == "search_object_by_name":
            object_name = function_args.get("object_name")
            return server.search_object_by_name(object_name)
        elif function_name == "summarize_objects":
            objects = function_args.get("objects")
            return server.summarize_objects(objects)
        elif function_name == "who_am_i":
            return server.who_am_i()
        elif function_name == "work_list":
            return server.work_list()
        else:
            return {
                "status": 200,
                "message": "Successfully ran function: " + function_name,
            }


if __name__ == "__main__":
    function_json = """
    {
        "api_name": "add_work_items_to_sprint",
        "arguments": {
            "work_ids": [
                "work_id_1",
                "work_id_2"
            ],
            "sprint_id": "sprint_id_1"
        }
    }
    """
    function_json = json.loads(function_json)
    api_tree = []
    executor = Executor()
    res = executor.run(function_json)
    if res is not None:
        res, execution_res = res
        print(execution_res)
