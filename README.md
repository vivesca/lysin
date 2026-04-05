# lysin

Cell biology term lookup — verify naming before building.

In cell biology, lysin is an enzyme that breaks down cell walls. This package
"breaks down" biological terminology into its component parts — **definition**,
**mechanism**, and **authoritative source URL** — so you can verify an analogy
is grounded in real biology before naming software after it.

## Why

When building software with biology-inspired names (trogocytosis, mitosis,
endocytosis), it's easy to pick a term that sounds right but doesn't match
the actual mechanism. `lysin` fetches the real definition from authoritative
sources and lets you decide whether the analogy holds.

## Install

```bash
# As an MCP server (Claude Code, Cursor, Windsurf, etc.)
uvx lysin

# As a Python library
pip install lysin
```

## Use

### MCP tool

Once configured in your MCP client, call the `lysin` tool with a term:

```
lysin("trogocytosis")
```

### Python library

```python
from lysin import fetch_summary

article = fetch_summary("trogocytosis")
print(article.definition)
print(article.mechanism)
print(article.url)
```

## Sources

- [UniProt](https://www.uniprot.org) — protein function and mechanism
- [Reactome](https://reactome.org) — biological pathways
- [Wikipedia](https://en.wikipedia.org) — general biology articles

## License

MIT
