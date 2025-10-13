import json
from datetime import datetime
import logging

logger = logging.getLogger("todo_log")

def load():
    try:
        with open("todo.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        logger.warning("todo.json not found, starting fresh.")
        return [], 1
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding todo.json: {e}")
        return [], 1
    except Exception as e:
        logger.error(f"Unexpected error loading todo.json: {e}")
        return [], 1

    tasks = data[0]
    for t in tasks:
        if t.get("due"):  # handle None safely
            try:
                t["due"] = datetime.strptime(t["due"], "%Y-%m-%d").date()
            except ValueError as e:
                logger.warning(f"Skipping invalid due date '{t['due']}': {e}")
                t["due"] = None
    next_id = data[1]
    return tasks, next_id

# def load():
#     try:
#         with open("todo.json", "r") as f:
#             data = json.load(f)
#     except:
#         data = [[], 1]
#     tasks = data[0]
#     for t in tasks:
#         t["due"] = datetime.strptime(t["due"], "%Y-%m-%d")
#     next_id = data[1]
#     return tasks, next_id

def save(tasks, next_id):
    data = [tasks, next_id]
    json_str = json.dumps(data, default=str)
    with open("todo.json", "w") as f:
        f.write(json_str)



