from mcp.server.fastmcp import FastMCP

mcp = FastMCP("statscan")

@mcp.tool()
def greet(name: str) -> str:
    "Say hello to someone"
    return f"Hello, {name}! Welcome to StatsCan MCP server!"

def main():
    mcp.run()