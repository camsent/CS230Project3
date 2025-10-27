import json
from datetime import datetime, timedelta

FORMAT_CODE = "%Y-%m-%d"

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

def save(json_input):
    with open("todo.json", "w") as f:
        f.write(json_input)

def load():
    with open("todo.json", "r") as f:
        json_string = f.read()
        return json_string
   
def load_user_list():
    with open("users.json", "r") as f:
        accounts = f.read()
        return accounts
   

current_login = {"username" : "_not_"}

NO_USER_MESSAGE = "You cannot access the task system without logging in."  
def user_check():
    if current_login["username"] == "_not_":
        return False


def find_date(start_date: datetime, end_date: datetime) -> str:
    json_string = load()
    if user_check == False:
        return NO_USER_MESSAGE
    data = open_json(json_string)
    new_data = {"tasks" : []}
    for task in data["tasks"]:
        due_date = datetime.strptime(task["due_date"], FORMAT_CODE)
        if due_date >= start_date and due_date <= end_date:
            if task["user_id"] == current_login["user_id"]:
                new_data["tasks"].append(task)
    new_string = close_json(new_data)
    return new_string

def all_tasks() -> str:
    json_string = load()
    if user_check == False:
        return NO_USER_MESSAGE
    data = open_json(json_string)
    new_data = {"tasks" : []}
    for task in data["tasks"]:
        if task["user_id"] == current_login["user_id"]:
            new_data["tasks"].append(task)
    new_string = close_json(new_data)
    return new_string

def create_task(description: str, due_date: str) -> str:
    json_string = load()
    if user_check == False:
        return NO_USER_MESSAGE
    data = open_json(json_string)
    task = {"id" : 900, "user_id" : current_login["user_id"], "description" : description, "due_date" : due_date}
    data["tasks"].append(task)
    json_string = close_json(data)
    save(json_string)
    return "Task created"

def delete_task(search_id: int) -> str:
    json_string = load()
    if user_check == False:
        return NO_USER_MESSAGE
    data = open_json(json_string)
    for task in data["tasks"]:
        if task["id"] == search_id and task["user_id"] == current_login["user_id"]:
            data["tasks"].remove(task)
            json_string = close_json(data)
            save(json_string)
            return "Task deleted"
    return "No task found with that id"

def update_description(search_id: int, description: str) -> str:
    json_string = load()
    if user_check == False:
        return NO_USER_MESSAGE
    data = open_json(json_string)
    for task in data["tasks"]:
        if task["id"] == search_id and task["user_id"] == current_login["user_id"]:
            task["description"] = description
            json_string = close_json(data)
            save(json_string)
            return "Task Updated"
    return "No task found with that id"

def update_date(search_id: int, due_date: str) -> str:
    json_string = load()
    if user_check == False:
        return NO_USER_MESSAGE
    data = open_json(json_string)
    for task in data["tasks"]:
        if task["id"] == search_id and task["user_id"] == current_login["user_id"]:
            task["due_date"] = due_date
            json_string = close_json(data)
            save(json_string)
            return "Task Updated"
    return "No task found with that id"

def check_login() -> str:
    if current_login["username"] == "_not_":
        return "not currently logged in."
    else:
        return "logged in"
   
def login(username: str) -> str:
    global current_login
    accounts = open_json(load_user_list())
    for account in accounts["accounts"]:
        if username == account["username"]:
            current_login = account
            return "logged in"
    return "Incorrect username"

def logout() -> str:
    global current_login
    current_login = {"username" : "_not_"}
    return "Logged out"
