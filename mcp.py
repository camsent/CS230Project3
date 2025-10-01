from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Price Finder")

@mcp.tool()
async def price(item: str) -> str:
    """Find the price of an item by it's name"""
    return(f"The price of {item} is 50$")


if __name__ == "__main__":
    mcp.run(transport="stdio")