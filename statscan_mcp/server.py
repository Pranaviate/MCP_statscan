from mcp.server.fastmcp import FastMCP

from statscan_mcp.tools.list_cubes import list_cubes
from statscan_mcp.tools.list_cubes_full import list_cubes_full
from statscan_mcp.tools.get_cube_metadata import get_cube_metadata
from statscan_mcp.tools.get_vector_data_by_range import get_vector_data_by_range
from statscan_mcp.tools.get_table import get_table
from statscan_mcp.tools.get_vector_info import get_vector_info


mcp = FastMCP("statscan")

@mcp.tool()
def greet(name: str) -> str:
    "Say hello to someone"
    return f"Hello, {name}! Welcome to StatsCan MCP server!"

mcp.tool()(list_cubes)
mcp.tool()(list_cubes_full)
mcp.tool()(get_cube_metadata)
mcp.tool()(get_vector_data_by_range)
mcp.tool()(get_table)
mcp.tool()(get_vector_info)

def main():
    mcp.run()