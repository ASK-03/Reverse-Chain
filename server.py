import uuid
import numpy as np


def add_work_items_to_sprint(work_ids, sprint_id):
    """
    Adds the given work items to the sprint.

    :param work_ids: A list of work item IDs to be added to the sprint.
    :param sprint_id: The ID of the sprint to which the work items should be added.
    :return: None
    """
    n = len(work_ids)
    # print(f"Added work items {work_ids} to sprint {sprint_id}.")

    work_items_id = [uuid.uuid1().hex for _ in range(n)]

    return {
        "work_ids": work_items_id,
        "status": 200,
        "message": f"Succesfully added work items to sprint by ids: {work_items_id}.",
    }


def create_actionable_tasks_from_text(text):
    """
    Given a text, extracts actionable insights, and creates tasks for them, which are kind of a work item.

    :param text: The text from which the actionable insights need to be created.
    :return: work_ids: list of work items created from the text.
    """
    work_ids = [uuid.uuid1().hex for _ in range(np.random.randint(1, 10))]

    return {
        "work_ids": work_ids,
        "status": 200,
        "message": f"Successfully created actionable tasks from text with work_ids: {work_ids}",
    }


def get_similar_work_items(work_id):
    """
    Returns a list of work items that are similar to the given work item.

    Args:
        work_id (str): The ID of the work item for which you want to find similar items.

    Returns:
        list: A list of work items that are similar to the given work item. Each item is a string.

    Example:
        get_similar_work_items("12345")
    """
    work_ids = [uuid.uuid1().hex for _ in range(np.random.randint(1, 10))]
    return {
        "work_ids": work_ids,
        "status": 200,
        "message": f"Successfully retrieved similar work items by work ids: {work_ids}.",
    }


def get_sprint_id():
    """
    Returns the ID of the current sprint.

    Returns:
        str: The ID of the current sprint.

    Example:
        get_sprint_id()
    """
    # Placeholder code for demonstration purposes
    # In a real scenario, this is where you would implement the logic to determine the current sprint ID
    current_sprint_id = "Sprint123"
    return {
        "sprint_id": current_sprint_id,
        "status": 200,
        "message": f"Successfully retrieved current sprint ID, {current_sprint_id}",
    }


def prioritize_objects(objects):
    """
    Returns a list of objects sorted by priority. The logic of what constitutes priority for a given object
    is an internal implementation detail.

    Args:
        objects (list): A list of objects to be prioritized.

    Returns:
        list: A list of objects that have been prioritized. Each object is a string.

    Example:
        prioritize_objects(["object3", "object1", "object2"])
    """
    prioritize_objects = [uuid.uuid1().hex for _ in range(np.random.randint(1, 3))]
    return {
        "prioritized_objects": prioritize_objects,
        "status": 200,
        "message": f"Successfully prioritized objects, object priority list is {prioritize_objects}.",
    }


def search_object_by_name(query):
    """
    Given a search string, returns the id of a matching object in the system of record.
    If multiple matches are found, it returns the one where the confidence is highest.

    Args:
        query (str): The search string, for example, customer\'s name, part name, username.

    Returns:
        list: The id(s) of the matching object(s) in the system of record.

    Example:
        search_object_by_name("customer_name")
    """
    # Placeholder code for demonstration purposes
    # In a real scenario, this is where you would implement the logic to search for the object by name
    # and return the corresponding id(s)
    matching_ids = ["id1", "id2", "id3"]
    return {
        "matching_ids": matching_ids,
        "status": 200,
        "message": f"Successfully searched for object by name. Matching ids: {', '.join(matching_ids) }",
    }


def summarize_objects(objects):
    """
    Summarizes a list of objects. The logic of how to summarize a particular object type
    is an internal implementation detail.

    Args:
        objects (list): A list of objects to summarize.

    Returns:
        str: A summary of the objects.

    Example:
        summarize_objects(["object1", "object2", "object3"])
    """
    # Placeholder code for demonstration purposes
    # In a real scenario, this is where you would implement the logic to summarize the given objects
    # The actual logic would depend on the specific object types and the summary criteria
    summary = (
        f"Summary of {len(objects) if objects is not None else 0} objects: {objects}"
    )
    return {
        "summary": summary,
        "status": 200,
        "message": "Successfully summarized objects.",
    }


def who_am_i():
    import uuid

    """
    Returns the string ID of the current user.

    Returns:
        str: The string ID of the current user.

    Example:
        who_am_i()
    """
    # Placeholder code for demonstration purposes
    # In a real scenario, this is where you would implement the logic to determine the current user ID
    current_user_id = uuid.uuid1().hex
    return {
        "user_id": current_user_id,
        "status": 200,
        "message": "Successfully retrieved current user ID. Current user ID: "
        + current_user_id,
    }


def work_list(
    applies_to_part=None,
    created_by=None,
    issue_priority=None,
    issue_rev_orgs=None,
    limit=50,
    owned_by=None,
    stage_name=None,
    ticket_needs_response=None,
    ticket_rev_org=None,
    ticket_severity=None,
    ticket_source_channel=None,
    work_type=None,
):
    """
    Returns a list of work items matching the request.

    Args:
        applies_to_part (list, optional): Filters for work belonging to any of the provided parts.
        created_by (list, optional): Filters for work created by any of these users.
        issue_priority (list, optional): Filters for issues with any of the provided priorities (p0, p1, p2, p3).
        issue_rev_orgs (list, optional): Filters for issues with any of the provided Rev organizations.
        limit (int, optional): The maximum number of works to return. The default is '50'.
        owned_by (list, optional): Filters for work owned by any of these users.
        stage_name (list, optional): Filters for records in the provided stage(s) by name.
        ticket_needs_response (bool, optional): Filters for tickets that need a response.
        ticket_rev_org (list, optional): Filters for tickets associated with any of the provided Rev organizations.
        ticket_severity (list, optional): Filters for tickets with any of the provided severities (blocker, high, low, medium).
        ticket_source_channel (list, optional): Filters for tickets with any of the provided source channels.
        work_type (list, optional): Filters for work of the provided types (issue, ticket, task).

    Returns:
        list: A list of work ids of the work items that match the request in filters.

    Example:
        work_list(applies_to_part=["part1", "part2"], created_by=["user1"], issue_priority=["p1", "p2"], limit=10)
    """
    work_items = [uuid.uuid1().hex for _ in range(np.random.randint(1, 3))]
    return {
        "work_items": work_items,
        "status": 200,
        "message": "Successfully retrieved work items. Work items: "
        + ", ".join(work_items),
    }
