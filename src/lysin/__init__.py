"""lysin — cell biology term lookup from UniProt, Reactome, and Wikipedia.

In cell biology, lysin is an enzyme that breaks down cell walls. This package
"breaks down" biological terminology into its component parts: definition,
mechanism, and authoritative source, before you use them to name software.
"""

from lysin.fetch import fetch_sections, fetch_summary

__version__ = "0.2.0"
__all__ = ["fetch_summary", "fetch_sections"]
