from mcp.server.fastmcp import FastMCP

from statscan_mcp.config import settings

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Unofficial MCP server for Statistics Canada's Web Data Service. Access 7,000+ datasets via 15 tools covering discovery, data retrieval, and change tracking.">
  <title>StatsCan MCP Server</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; color: #222; }
    h1 { font-size: 1.8rem; margin-bottom: 0.25rem; }
    h2 { margin-top: 2rem; }
    .subtitle { color: #555; margin-bottom: 2rem; }
    .endpoint { background: #f4f4f4; border: 1px solid #ddd; border-radius: 6px; padding: 0.75rem 1rem; font-family: monospace; font-size: 0.95rem; }
    table { width: 100%; border-collapse: collapse; margin-top: 0.75rem; }
    th { text-align: left; padding: 0.5rem; border-bottom: 2px solid #ddd; color: #444; }
    td { padding: 0.5rem; border-bottom: 1px solid #eee; vertical-align: top; }
    td:first-child { font-family: monospace; color: #0066cc; white-space: nowrap; padding-right: 1.5rem; }
    .links { margin-top: 2rem; display: flex; gap: 1.5rem; }
    a { color: #0066cc; }
    footer { margin-top: 3rem; color: #888; font-size: 0.85rem; border-top: 1px solid #eee; padding-top: 1rem; }
  </style>
</head>
<body>
  <h1>StatsCan MCP Server</h1>
  <p class="subtitle">
    Unofficial MCP server for Statistics Canada's Web Data Service (WDS) API.<br>
    Search and retrieve economic, demographic, and social data from ~7,000 StatsCan datasets.
  </p>

  <h2>MCP Endpoint</h2>
  <div class="endpoint">https://pranaviate-statscan-mcp.hf.space/mcp</div>

  <h2>15 Available Tools</h2>
  <table>
    <thead><tr><th>Tool</th><th>Purpose</th></tr></thead>
    <tbody>
      <tr><td>list_cubes</td><td>Search datasets by keyword (lightweight)</td></tr>
      <tr><td>list_cubes_full</td><td>Search datasets with full metadata</td></tr>
      <tr><td>get_cube_metadata</td><td>Get dimensions and structure of a dataset</td></tr>
      <tr><td>get_vector_info</td><td>Metadata for a specific time series</td></tr>
      <tr><td>get_vector_data_by_range</td><td>Fetch one time series by date range</td></tr>
      <tr><td>get_table</td><td>Fetch rectangular data by cube + coordinates</td></tr>
      <tr><td>get_series_info</td><td>Series info by cube ID + coordinates</td></tr>
      <tr><td>get_changed_cubes</td><td>Datasets updated on a given date</td></tr>
      <tr><td>get_changed_series</td><td>Series updated today</td></tr>
      <tr><td>get_changed_vector_data</td><td>Changed data for a specific vector</td></tr>
      <tr><td>get_changed_series_data</td><td>Changed data by cube + coordinates</td></tr>
      <tr><td>get_vectors_latest</td><td>Multiple vectors, latest N periods</td></tr>
      <tr><td>get_bulk_vectors</td><td>Bulk vector data by date range</td></tr>
      <tr><td>get_full_table_csv</td><td>Download URL for full table (CSV)</td></tr>
      <tr><td>get_full_table_sdmx</td><td>Download URL for full table (SDMX)</td></tr>
    </tbody>
  </table>

  <div class="links">
    <a href="https://github.com/Pranaviate/MCP_statscan">GitHub</a>
    <a href="https://smithery.ai/server/pranaviate/statscan-mcp">Smithery</a>
    <a href="https://www.statcan.gc.ca/en/developers/wds">StatsCan WDS Docs</a>
  </div>

  <footer>Built with Python + FastMCP &middot; Data from Statistics Canada WDS API</footer>
</body>
</html>"""

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
    if settings.transport == "http":
        from starlette.middleware.cors import CORSMiddleware
        from starlette.responses import HTMLResponse, JSONResponse

        class _HomepageMiddleware:
            def __init__(self, app):
                self.app = app

            async def __call__(self, scope, receive, send):
                if scope["type"] == "http" and scope["path"] == "/":
                    response = HTMLResponse(HTML)
                    await response(scope, receive, send)
                elif scope["type"] == "http" and scope["path"] == "/health":
                    response = JSONResponse({"status": "ok"})
                    await response(scope, receive, send)
                else:
                    await self.app(scope, receive, send)

        mcp_asgi = mcp.streamable_http_app()

        app = CORSMiddleware(
            _HomepageMiddleware(mcp_asgi),
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["mcp-session-id"],
        )

        import uvicorn

        uvicorn.run(app, host="0.0.0.0", port=settings.port)
    else:
        mcp.run()