from datetime import datetime, timedelta
import logging
import json_save

tasks, next_id = [], 1

started = False

logger = logging.getLogger("todo_log")
logging.basicConfig(filename='todo.log', filemode='w', level=logging.INFO)

def start_todo():
    global tasks, next_id, started 
    if not started:
        logger.info("Todo Started")
        logger.info("Loading JSON data")
        tasks, next_id = json_save.load()
        logger.info(f"Loaded JSON data: {tasks, next_id}")
        started = True

def add_task(description: str) -> str:
    start_todo()
    global next_id
    tasks.append({"id": next_id, "description": description, "due": None})
    current_id = next_id
    next_id += 1
    logger.info(f"Task added: {description}")
    logger.info(f"Saving task list...")
    json_save.save(tasks, next_id)
    logger.info(f"Task list saved")
    return f"Task added: {description} with ID: {current_id}"

def list_tasks() -> list[str]:
    start_todo()
    if not tasks:
        return ["No tasks."]

    completed = []
    todo_list = []

    for t in tasks:
        entry = (
            f"{t['id']} - {t['description']} "
            f"(Due: {t['due'] or 'No due date'}) "
            f"[{'Done' if t.get('done', False) else 'Not done'}]"
        )
        if t.get("done", False):
            completed.append(entry)
        else:
            todo_list.append(entry)

    output = []
    if todo_list:
        output.append("📌 To-Do:")
        output.extend(todo_list)
    if completed:
        output.append("\n✅ Completed:")
        output.extend(completed)

    return output

def delete_task(task_id: int) -> str:
    start_todo()
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    logger.info(f"Deleted task {task_id}")
    logger.info(f"Saving task list...")
    json_save.save(tasks, next_id)
    logger.info(f"Task list saved")
    return f"Deleted task {task_id}"

def set_due_date(task_id: int, due_date: datetime) -> str:
    start_todo()
    for t in tasks:
        if t["id"] == task_id:
            try:
                t["due"] = due_date
                logger.info(f"Due date set for task {task_id}: {due_date}")
                logger.info(f"Saving task list...")
                json_save.save(tasks, next_id)
                logger.info(f"Task list saved")
                return f"Due date set for task {task_id}: {due_date}"
            except ValueError:
                logger.info("Invalid date format. Use YYYY-MM-DD.")
                return "Invalid date format. Use YYYY-MM-DD."
    return f"Task {task_id} not found."

def search_date(target_date: str) -> list[str]:
    """
    Find tasks with a specific due date.
    target_date must be in YYYY-MM-DD format.
    """
    start_todo()
    try:
        date_obj = datetime.strptime(target_date, "%Y-%m-%d").date()
    except ValueError:
        return [f"Invalid date format: {target_date}. Use YYYY-MM-DD."]

    matches = [t for t in tasks if t["due"] == date_obj]
    if not matches:
        return [f"No tasks due on {target_date}."]
    return [f"{t['id']} - {t['description']} (Due: {t['due']})" for t in matches]

def recurring_tasks(task: str, days: list[str], end_date: str) -> str:
    """
    Create recurring tasks until end_date.
    - task: task description
    - days: weekdays, e.g. ["Monday", "Wednesday"]
    - end_date: YYYY-MM-DD format
    """
    start_todo()
    try:
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD."

    today = datetime.today().date()
    created = []

    # Normalize weekdays
    weekdays = {d.capitalize() for d in days}
    valid_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    if not weekdays.issubset(valid_days):
        return f"Invalid weekday(s). Choose from: {', '.join(valid_days)}"

    current = today
    while current <= end:
        if current.strftime("%A") in weekdays:
            # add_task increments next_id automatically
            description = f"{task} (Recurring on {current.strftime('%A')})"
            add_task(description)

            # find the task we just added (last one in list)
            new_task = tasks[-1]
            set_due_date(new_task["id"], current)

            created.append(f"{new_task['id']} - {description} (Due: {current.strftime('%Y-%m-%d')})")
        current += timedelta(days=1)

    if not created:
        return "No tasks created — check your dates and weekdays."

    return "Created recurring tasks:\n" + "\n".join(created)

def mark_done(task_id: int) -> str:
    start_todo()
    for t in tasks:
        if t["id"] == task_id:
            # If the "done" key is missing, create it
            t["done"] = True
            logger.info(f"Marked task {task_id} as completed.")
            json_save.save(tasks, next_id)
            return f"Task {task_id} marked as completed."
    return f"Task {task_id} not found."


def get_reminders() -> list[str]:
    start_todo()
    """Return tasks due today or tomorrow."""
    today = datetime.today().date()
    tomorrow = today + timedelta(days=1)
    upcoming = [t for t in tasks if t["due"] in [today, tomorrow]]
    if not upcoming:
        return ["No reminders."]
    logger.info(f"Upcoming task list: {upcoming}")
    #Return tasks instead of strings
    return [f"Reminder: {t['id']} - {t['description']} (Due: {t['due']})" for t in upcoming]
