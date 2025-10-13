from mcp.server.fastmcp import FastMCP
from datetime import datetime, timedelta
import main

mcp = FastMCP("My Task")

@mcp.tool()
async def add(task: str) -> str:
    """Add a new task to the list."""
    return main.add_task(task)

@mcp.tool()
async def delete(task_id: int):
    """Delete a task by its ID."""
    return main.delete_task(task_id)

@mcp.tool()
async def list_all() -> str:
    """List all tasks, dont display IDs"""
    return "\n".join(main.list_tasks())

@mcp.tool()
async def update(task_id: int, new_task: str) -> str:
    """Update an existing task by ID."""
    return main.update_task(task_id, new_task)

@mcp.tool()
async def mark_done(task_id: int) -> str:
    """Mark a task as completed."""
    return main.mark_done(task_id)

@mcp.tool()
async def set_due_date(task_id: int, due_date: str) -> str:
    """
    Set a due date for a task.
    due_date should be in YYYY-MM-DD format.
    """
    date = datetime.strptime(due_date, "%Y-%m-%d").date()
    return main.set_due_date(task_id, date)

@mcp.tool()
async def get_reminders() -> str:
    """Get tasks that are due today or tomorrow."""
    reminders = main.get_reminders()
    return "\n".join(reminders)

@mcp.tool()
async def search_date(target_date: str) -> str:
    """Search tasks by due date (YYYY-MM-DD)."""
    return "\n".join(main.search_date(target_date))


@mcp.tool()
async def recurring_tasks(task: str, days: list[str], end_date: str) -> str:
    """
    Create recurring tasks.
    Generates a task for each selected weekday until the given end date.
    - task: the task description
    - days: list of weekdays, e.g. ["Monday", "Wednesday"]
    - end_date: in YYYY-MM-DD format
    """
    return main.recurring_tasks(task, days, end_date)

if __name__ == "__main__":
    mcp.run(transport="stdio")