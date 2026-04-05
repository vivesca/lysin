"""MCP server for lysin — cell biology term lookup."""

from __future__ import annotations

from fastmcp import FastMCP

from lysin.fetch import fetch_summary

app = FastMCP("lysin")


@app.tool()
def lysin(term: str) -> str:
    """Look up real cell biology for a term — definition, mechanism, source URL.

    Sources: UniProt, Reactome, Wikipedia. Use before naming any software component
    after a biological concept to verify the analogy is grounded in real biology.
    """
    try:
        article = fetch_summary(term)
    except LookupError as exc:
        return str(exc)

    return "\n".join([
        f"# {article.title}",
        f"Source: {', '.join(article.sources)}",
        "",
        f"**Definition:** {article.definition}",
        "",
        f"**Mechanism:** {article.mechanism}",
        "",
        f"**URL:** {article.url}",
    ])


def main() -> None:
    """CLI entry point for `uvx lysin-mcp`."""
    app.run(transport="stdio")


if __name__ == "__main__":
    main()
