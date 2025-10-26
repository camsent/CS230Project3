import json
from datetime import datetime, timedelta

FORMAT_CODE = "%Y-%m-%d"

# THIS IS MY HARDCODED JSON STRING. THIS FORMAT IS WHAT MY CODE IS EXPECTING, BUT IT CAN BE EASILY CHANGED.

json_string =   """
                    {
                    "tasks": [
                        {
                        "id": 1,
                        "description": "Complete project proposal and submit for review",
                        "due_date": "2025-10-31"
                        },
                        {
                        "id": 2,
                        "description": "Review team feedback and update documentation",
                        "due_date": "2025-11-05"
                        },
                        {
                        "id": 3,
                        "description": "Prepare presentation for stakeholders",
                        "due_date": "2025-11-10"
                        },
                        {
                        "id": 4,
                        "description": "Schedule follow-up meeting with client",
                        "due_date": "2025-11-08"
                        }
                    ]
                    }
                """

# THESE FUNCTIONS ARE ESSENTIALLY TOOLS TO MAKE THINGS EASIER FOR ME IN SOME OF THE OTHER FUNCTIONS, THEY ARE FINE.

def open_json(json_input):
    json_object = json.loads(json_input)
    return json_object

def close_json(json_object):
    json_string = json.dumps(json_object)
    return json_string

def get_month(month: int, year: int):
    start_date = datetime.strptime(f"{year}-{month}-1", FORMAT_CODE)
    end_date = datetime.strptime(f"{year}-{month + 1}-1", FORMAT_CODE) - timedelta(days=1)
    return start_date, end_date

# THESE FUNCTIONS ARE BASICALLY FINISHED, THEY ONLY NEED DATA TO BE DIRECTLY FROM THE BACKEND RATHER THAN MY HARDCODED JSON STRING.

def find_date(start_date: datetime, end_date: datetime):
    data = open_json(json_string)
    new_data = {"tasks" : []}
    for task in data["tasks"]:
        due_date = datetime.strptime(task["due_date"], FORMAT_CODE)
        if due_date >= start_date and due_date <= end_date:
            new_data["tasks"].append(task)
    new_string = close_json(new_data)
    return new_string

def all_tasks():
    return json_string
        
# THIS SECTION DEALS WITH CREATING, DELETING AND UPDATING TASKS. IT REALLY NEEDS BACKEND TO MAKE IT WORK.
# ALMOST NONE OF THIS CODE IS REALLY USABLE, AS MOST OF IT DEALS WITH UPDATING A RANDOM ASS JSON STRING.

def create_task(description: str, due_date: str):
    # ID IS HARDCODED TO 900 HERE, I GUESS ID IS DECIDED BY THE BACKEND?
    global json_string
    data = open_json(json_string)
    task = {"id" : 900, "description" : description, "due_date" : due_date}
    data["tasks"].append(task)
    # THIS IS WHERE THE TASK SHOULD ACTUALLY BE ADDED
    data_string = close_json(data)
    json_string = data_string
    #/
    return "Task created"

def delete_task(search_id: int):
    global json_string
    data = open_json(json_string)
    for task in data["tasks"]:
        if task["id"] == search_id:
            data["tasks"].remove(task)
            # THIS LINE NEEDS TO BE REPLACED WITH A CONNECTION TO BACKEND
            data_string = close_json(data)
            json_string = data_string
            #/
            return "Task deleted"
    return "No task found with that id"

def update_description(search_id: int, description: str):
    global json_string
    data = open_json(json_string)
    for task in data["tasks"]:
        if task["id"] == search_id:
            task["description"] = description
            # THIS LINE NEEDS TO BE REPLACED WITH A CONNECTION TO BACKEND
            data_string = close_json(data)
            json_string = data_string
            #/
            return "Task Updated"
    return "No task found with that id"
    

def update_date(search_id: int, due_date: str):
    global json_string
    data = open_json(json_string)
    for task in data["tasks"]:
        if task["id"] == search_id:
            task["due_date"] = due_date
            # THIS LINE NEEDS TO BE REPLACED WITH A CONNECTION TO BACKEND
            data_string = close_json(data)
            json_string = data_string
            #/
            return "Task Updated"
    return "No task found with that id"