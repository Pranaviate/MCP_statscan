import os

from mcp.server.fastmcp import FastMCP

from statscan_mcp.tools.list_cubes import list_cubes
from statscan_mcp.tools.list_cubes_full import list_cubes_full
from statscan_mcp.tools.get_cube_metadata import get_cube_metadata
from statscan_mcp.tools.get_vector_data_by_range import get_vector_data_by_range
from statscan_mcp.tools.get_table import get_table
from statscan_mcp.tools.get_vector_info import get_vector_info
from statscan_mcp.tools.get_series_info import get_series_info
from statscan_mcp.tools.get_changed_cubes import get_changed_cubes
from statscan_mcp.tools.get_changed_series import get_changed_series
from statscan_mcp.tools.get_changed_vector_data import get_changed_vector_data
from statscan_mcp.tools.get_changed_series_data import get_changed_series_data
from statscan_mcp.tools.get_vectors_latest import get_vectors_latest
from statscan_mcp.tools.get_bulk_vectors import get_bulk_vectors
from statscan_mcp.tools.get_full_table_csv import get_full_table_csv
from statscan_mcp.tools.get_full_table_sdmx import get_full_table_sdmx


mcp = FastMCP("statscan")

mcp.tool()(list_cubes)
mcp.tool()(list_cubes_full)
mcp.tool()(get_cube_metadata)
mcp.tool()(get_vector_data_by_range)
mcp.tool()(get_table)
mcp.tool()(get_vector_info)
mcp.tool()(get_series_info)
mcp.tool()(get_changed_cubes)
mcp.tool()(get_changed_series)
mcp.tool()(get_changed_vector_data)
mcp.tool()(get_changed_series_data)
mcp.tool()(get_vectors_latest)
mcp.tool()(get_bulk_vectors)
mcp.tool()(get_full_table_csv)
mcp.tool()(get_full_table_sdmx)

def main():
    transport = os.environ.get("TRANSPORT", "stdio")

    if transport == "http":
        from starlette.middleware.cors import CORSMiddleware

        app = mcp.streamable_http_app()
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["mcp-session-id"],
        )

        import uvicorn

        port = int(os.environ.get("PORT", 8080))
        uvicorn.run(app, host="0.0.0.0", port=port)
    else:
        mcp.run()