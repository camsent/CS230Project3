from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My Tasks")

@mcp.tool()
async def ping() -> str:
    """returns a pong"""
    return "pong"

@mcp.tool()
async def calendar() -> str:
    """returns a calendar with an asterisk under it for each day that has a task and a space under it for each day that doesn't have a task."""
    return "October 18th and 19th and 4th and 3rd"

@mcp.tool()
async def list_tasks() -> str:
    """lists all the tasks in date order."""
    return """
        {
        "tasks": [
            {
            "id": "task_001",
            "description": "Complete project proposal and submit for review",
            "due_date": "2025-10-31"
            },
            {
            "id": "task_002",
            "description": "Review team feedback and update documentation",
            "due_date": "2025-11-05"
            },
            {
            "id": "task_003",
            "description": "Prepare presentation for stakeholders",
            "due_date": "2025-11-10"
            },
            {
            "id": "task_004",
            "description": "Schedule follow-up meeting with client",
            "due_date": "2025-11-08"
            }
        ]
        }
    """

@mcp.tool()
async def display_task() -> str:
    """Display a single randomly selected task from the task list"""
    return """
        { "id": "task_001", "description": "Complete project proposal and submit for review", "due_date": "2025-10-31"}
    """

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