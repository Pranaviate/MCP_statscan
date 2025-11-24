import asyncio

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.server import InitializationOptions

server = Server("statscan")

async def run_server():
      async with stdio_server() as (read_stream, write_stream):
          await server.run(
              read_stream,
              write_stream,
              server.create_initialization_options()
          )

def main():
      asyncio.run(run_server())





