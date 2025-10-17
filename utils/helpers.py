from datetime import datetime

def format_timestamp() -> str:
    """Return formatted timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text to specified length"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def validate_file_size(file, max_size_mb: int) -> bool:
    """Check if file size is within limit"""
    file_size_mb = file.size / (1024 * 1024)
    return file_size_mb <= max_size_mb