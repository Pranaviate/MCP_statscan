---
title: StatsCan MCP Server
emoji: 📊
colorFrom: red
colorTo: blue
sdk: docker
pinned: false
---

# statscan-mcp

An [MCP](https://modelcontextprotocol.io/) server that lets AI agents query Statistics Canada's live data. Connect it to Claude Desktop, Cursor, or any MCP-compatible client and ask questions about Canadian economic indicators — the agent discovers datasets, pulls time series, and cites sources automatically.

Covers the full [Web Data Service (WDS)](https://www.statcan.gc.ca/en/developers/wds) API — all 15 endpoints — with no API key required.

![Python 3.11](https://img.shields.io/badge/python-3.11-blue)
![MIT License](https://img.shields.io/badge/license-MIT-green)
[![Smithery](https://smithery.ai/badge/pranaviate/statscan-mcp)](https://smithery.ai/server/pranaviate/statscan-mcp)

## What's Inside

- **15 async tools** covering discovery, data retrieval, bulk downloads, and change tracking
- **Shared API client** (`WDSClient`) — centralized HTTP logic, connection reuse, error handling in one place
- **Dual transport** — runs locally via stdio or remotely via Streamable HTTP (one env var to switch)
- **Docker-ready** — `Dockerfile` + `smithery.yaml` for one-click deployment on Smithery.ai
- **Tested** — 16 unit tests with mocked HTTP, no live API calls, runs in under 3 seconds
- **Production-ready** — structured logging, retry logic with exponential backoff, configurable timeouts, `/health` endpoint

## Tools

### Discovery & Metadata
| Tool | Description |
|------|-------------|
| `list_cubes` | Search datasets by keyword (lightweight) |
| `list_cubes_full` | Full dataset list with more detail |
| `get_cube_metadata` | Dimensions, members, coverage for a dataset |
| `get_vector_info` | Metadata for a specific vector |
| `get_series_info` | Series info by cube + coordinates |

### Data Access
| Tool | Description |
|------|-------------|
| `get_vector_data_by_range` | Time series by date range |
| `get_table` | Rectangular data slice (latest N periods) |
| `get_vectors_latest` | Multiple vectors, latest N periods |
| `get_bulk_vectors` | Bulk vector data by date range |
| `get_full_table_csv` | Download URL for full table (CSV) |
| `get_full_table_sdmx` | Download URL for full table (SDMX) |

### Change Tracking
| Tool | Description |
|------|-------------|
| `get_changed_cubes` | Datasets updated since a date |
| `get_changed_series` | Series updated since a date |
| `get_changed_vector_data` | Changed data by vector |
| `get_changed_series_data` | Changed data by coordinates |

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `/mcp` | MCP protocol endpoint |
| `/health` | Health check — returns `{"status": "ok"}` |
| `/` | This landing page |

MCP endpoint: `https://pranaviate-statscan-mcp.hf.space/mcp`

### One-click via Smithery

[![Smithery](https://smithery.ai/badge/pranaviate/statscan-mcp)](https://smithery.ai/server/pranaviate/statscan-mcp)

Visit **[smithery.ai/server/pranaviate/statscan-mcp](https://smithery.ai/server/pranaviate/statscan-mcp)** and click Install next to your client.

---

### Claude Desktop

Settings → Connectors → Add MCP Server → paste the endpoint URL above.

---

### Cursor

Add to `.cursor/mcp.json` in your project root (or `~/.cursor/mcp.json` for global):

```json
{
  "mcpServers": {
    "statscan": {
      "url": "https://pranaviate-statscan-mcp.hf.space/mcp"
    }
  }
}
```

---

### Windsurf

Add to `~/.codeium/windsurf/mcp_config.json` (macOS/Linux) or `%USERPROFILE%\.codeium\windsurf\mcp_config.json` (Windows):

```json
{
  "mcpServers": {
    "statscan": {
      "url": "https://pranaviate-statscan-mcp.hf.space/mcp"
    }
  }
}
```

---

### Cline (VS Code)

MCP Servers panel → Configure MCP Servers → add to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "statscan": {
      "url": "https://pranaviate-statscan-mcp.hf.space/mcp",
      "type": "streamableHttp"
    }
  }
}
```

---

### VS Code + GitHub Copilot

Open Command Palette → `MCP: Open User Configuration` → add to `mcp.json`:

```json
{
  "servers": {
    "statscan": {
      "type": "http",
      "url": "https://pranaviate-statscan-mcp.hf.space/mcp"
    }
  }
}
```

Requires VS Code 1.99+.

---

## Local Development

```bash
# MCP Inspector (stdio)
uv run mcp dev statscan_mcp/server.py

# HTTP transport
set TRANSPORT=http && uv run python -m statscan_mcp
# Server starts on http://localhost:7860
```

## License

MIT - [Pranav Sharma](https://github.com/Pranaviate)
