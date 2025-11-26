from mcp.server.fastmcp import FastMCP
from statscan_mcp.tools.list_cubes import list_cubes

mcp = FastMCP("statscan")

@mcp.tool()
def greet(name: str) -> str:
    "Say hello to someone"
    return f"Hello, {name}! Welcome to StatsCan MCP server!"

mcp.tool()(list_cubes)

def main():
    mcp.run()