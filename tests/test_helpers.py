import pytest
from utils.helpers import format_timestamp, truncate_text, validate_file_size

def test_truncate_text():
    """Test text truncation"""
    text = "This is a long text that needs to be truncated"
    result = truncate_text(text, max_length=10)
    assert len(result) <= 13  # 10 + "..."
    assert result.endswith("...")

def test_truncate_text_short():
    """Test that short text is not truncated"""
    text = "Short"
    result = truncate_text(text, max_length=10)
    assert result == text
    assert not result.endswith("...")

def test_format_timestamp():
    """Test timestamp formatting"""
    result = format_timestamp()
    assert isinstance(result, str)
    assert len(result) > 0