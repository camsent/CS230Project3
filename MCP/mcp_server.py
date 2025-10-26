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
    Returns a list of each task in order of due date, with the assignments with the soonest due date coming first. 
    The tasks are not already ordered by date, so they may need to be reorgonized."""
    if month == 0 and year == 0:
        tasks = mcp_helper.all_tasks()
    else:
        startdate, enddate = mcp_helper.get_month(month, year)
        tasks = mcp_helper.find_date(startdate, enddate)
    return tasks

@mcp.tool()
async def create_task(description: str, due_date: str) -> str:
    """Adds a task to the list of tasks. Date uses yyyy-mm-dd format"""
    return mcp_helper.create_task(description, due_date)

@mcp.tool()
async def update_task_description(id: int, description: str) -> str:
    """Updates a task from the user's task list. Task ids can be found by listing all tasks."""
    return mcp_helper.update_description(id, description)

@mcp.tool()
async def update_task_date(id: int, due_date: str) -> str:
    """Updates a task from the user's task list. Task ids can be found by listing all tasks. Date uses yyyy-mm-dd format"""
    return mcp_helper.update_description(id, due_date)

@mcp.tool()
async def delete_task(id: int) -> str:
    """Deletes a task from the user's task list. Task ids can be found by listing all tasks."""
    return mcp_helper.delete_task(id)

@mcp.tool()
async def am_i_logged_in() -> str:
    """Checks if the MCP server is currently logged into any account."""
    return mcp_helper.check_login()

@mcp.tool()
async def login_user(username: str, password: str) -> str:
    """Logs into a user account using a provided username and password"""
    return mcp_helper.login(username, password)

@mcp.tool()
async def logout_user() -> str:
    """If the user is logged in, logs out of that account"""
    return mcp_helper.logout()

if __name__ == "__main__":
    mcp.run(transport="stdio")