from statscan_mcp.server import HTML
from statscan_mcp import __version__


def test_html_renders():
    """HTML template must evaluate without errors (catches broken f-string braces)."""
    assert isinstance(HTML, str)
    assert len(HTML) > 0


def test_html_contains_version():
    """HTML footer must include the current package version."""
    assert __version__ in HTML
