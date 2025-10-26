from mcp.server.fastmcp import FastMCP
from datetime import datetime
import mcp_helper

FORMAT_CODE = "%Y-%m-%d"

mcp = FastMCP("My Tasks")

@mcp.tool()
async def calendar(month: int, year: int) -> str:
    """Takes the numerical form of the month and year requested.
    Returns a calendar with an asterisk under it for each day that has a task and a space under it for each day that doesn't have a task."""
    startdate, enddate = mcp_helper.get_month(month, year)
    tasks = mcp_helper.find_date(startdate, enddate)

    return tasks

@mcp.tool()
async def list_tasks(month: int, year: int) -> str:
    """Takes the numeral form of the month and year requested. If no month is requested, put 0 for both month and year.
    Returns a list of each task in order of due date, with the assignments with the soonest due date coming first."""
    if month == 0 and year == 0:
        tasks = mcp_helper.all_tasks()
    else:
        startdate, enddate = mcp_helper.get_month(month, year)
        tasks = mcp_helper.find_date(startdate, enddate)
    return tasks

@mcp.tool()
async def create_task(title: str, description: str, due_date: str) -> str:
    """Adds a task to the list of tasks"""
    return "Task added"

@mcp.tool()
async def update_task(title: str, description: str, due_date: str) -> str:
    """Removes the task with the same title and creates a new task with updated information"""
    return "Task updated"

@mcp.tool()
async def delete_task(title: str) -> str:
    """Deletes a task from the task list by its title"""
    return "Task deleted"

@mcp.tool()
async def am_i_logged_in() -> str:
    """Checks if the MCP server is currently logged into any account. If so, display the username of the account."""
    return "Not logged in"

@mcp.tool()
async def login_user(username: str, password: str) -> str:
    """Logs into a user accoun using a provided username and password"""
    return "User logged in"

@mcp.tool()
async def logout_user() -> str:
    """If the user is logged in, logs out of that account"""
    return "User logged out"

if __name__ == "__main__":
    mcp.run(transport="stdio")

"MCP Tools:"
"-Task Management"
"--Create Task"
"--List Tasks"
"--Update Task"
"--Delete Task"
"-User Management"
"--Login"
"--Logout"