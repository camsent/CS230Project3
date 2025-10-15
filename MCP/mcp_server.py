from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My Tasks")

@mcp.tool()
async def ping() -> str:
    """returns a pong"""
    return "pong"

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