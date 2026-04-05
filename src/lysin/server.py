        """MCP server for lysin — standalone or mountable into vivesca."""

        from __future__ import annotations

        from fastmcp import FastMCP

        from lysin import core

        app = FastMCP("lysin")


        @app.tool()
def lysin(**kwargs):
    """"""
    return core.lysin(**kwargs)


        def main() -> None:
            app.run(transport="stdio")


        if __name__ == "__main__":
            main()
