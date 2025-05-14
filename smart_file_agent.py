from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("SmartFileAgent")

@mcp.tool()
def list_files(path: str) -> list:
    """List all files in a given directory path."""
    return os.listdir(path)

@mcp.tool()
def read_file(path: str) -> str:
    """Return full text content of a file."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

@mcp.tool()
def get_file_size(path: str) -> str:
    """Return human-readable size of a file."""
    size = os.path.getsize(path)
    return f"{round(size / 1024, 2)} KB"


if __name__ == "__main__":
     mcp.run()
