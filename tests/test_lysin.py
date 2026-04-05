"""Tests for lysin."""

from unittest.mock import patch


def test_import():
    import lysin
    assert lysin.__version__ == "0.2.0"


def test_fetch_summary_exported():
    from lysin import fetch_summary
    assert callable(fetch_summary)


def test_server_creates_app():
    from lysin.server import app
    assert app.name == "lysin"


def test_lookup_unknown_term_returns_error():
    """Looking up a nonsense term returns a LookupError message, not a crash."""
    from lysin.server import lysin

    with patch("lysin.server.fetch_summary") as mock_fetch:
        mock_fetch.side_effect = LookupError("Term 'xyz' not found")
        result = lysin("xyz")
        assert "not found" in result
