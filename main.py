import os

from fastmcp import FastMCP


mcp = FastMCP("fastmcp-remote-server")


@mcp.tool
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def main() -> None:
    """Run the MCP server over HTTP."""
    host = os.getenv("FASTMCP_HOST", "0.0.0.0")
    port = int(os.getenv("FASTMCP_PORT", "8000"))
    mcp.run(transport="http", host=host, port=port)


if __name__ == "__main__":
    main()