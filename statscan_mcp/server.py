from mcp.server.fastmcp import FastMCP

from statscan_mcp.tools.list_cubes import list_cubes
from statscan_mcp.tools.get_cube_metadata import get_cube_metadata
from statscan_mcp.tools.get_series_by_vector import get_series_by_vector
from statscan_mcp.tools.get_table import get_table

mcp = FastMCP("statscan")

@mcp.tool()
def greet(name: str) -> str:
    "Say hello to someone"
    return f"Hello, {name}! Welcome to StatsCan MCP server!"

mcp.tool()(list_cubes)
mcp.tool()(get_cube_metadata)
mcp.tool()(get_series_by_vector)
mcp.tool()(get_table)

def main():
    mcp.run()