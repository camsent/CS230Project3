import json
from datetime import datetime, timedelta

FORMAT_CODE = "%Y-%m-%d"

json_string =   """
                    {
                    "tasks": [
                        {
                        "title": "Project Proposal",
                        "description": "Complete project proposal and submit for review",
                        "due_date": "2025-10-31"
                        },
                        {
                        "title": "Review team feedback",
                        "description": "Review team feedback and update documentation",
                        "due_date": "2025-11-05"
                        },
                        {
                        "title": "Prepare presentation",
                        "description": "Prepare presentation for stakeholders",
                        "due_date": "2025-11-10"
                        },
                        {
                        "id": "Schedule follow-up",
                        "description": "Schedule follow-up meeting with client",
                        "due_date": "2025-11-08"
                        }
                    ]
                    }
                """

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
        


def find_title():
    pass

start_date = datetime(2025, 11, 5)
end_date = datetime(2025, 11, 9)

find_date(get_month(11, 2025)[0], get_month(11, 2025)[1])