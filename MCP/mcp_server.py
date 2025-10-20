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
    return "Math homework on October 18th, Science homework on October 19th"

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