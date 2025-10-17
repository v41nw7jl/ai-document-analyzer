# API Documentation

## Claude Service API

### ClaudeService Class

Main service for interacting with Claude API.

#### Methods

##### `__init__()`
Initialize the Claude service with API credentials.
```python
service = ClaudeService()
```

##### `analyze_text(text: str, question: str = None) -> str`
Analyze document text with optional specific question.

**Parameters:**
- `text` (str): Document text to analyze
- `question` (str, optional): Specific question about the document

**Returns:**
- `str`: Claude's analysis response

**Example:**
```python
response = service.analyze_text(
    text="Document content here",
    question="What is the main topic?"
)
```

##### `summarize(text: str, length: str = "medium") -> str`
Generate summary of provided text.

**Parameters:**
- `text` (str): Text to summarize
- `length` (str): Summary length - "short", "medium", or "long"

**Returns:**
- `str`: Summary text

**Example:**
```python
summary = service.summarize(
    text="Long document text",
    length="short"
)
```

---

## File Handler API

### FileHandler Class

Handles file processing operations.

#### Static Methods

##### `extract_text_from_pdf(file) -> str`
Extract text from PDF file.

**Parameters:**
- `file`: Uploaded file object (BytesIO)

**Returns:**
- `str`: Extracted text

**Raises:**
- `Exception`: If PDF cannot be read

##### `extract_text_from_txt(file) -> str`
Extract text from TXT file.

**Parameters:**
- `file`: Uploaded file object

**Returns:**
- `str`: File content

##### `get_file_extension(filename: str) -> Optional[str]`
Get file extension from filename.

**Parameters:**
- `filename` (str): Name of the file

**Returns:**
- `str` or `None`: File extension in lowercase

---

## Helper Functions

### `truncate_text(text: str, max_length: int = 100) -> str`
Truncate text to specified length.

### `validate_file_size(file, max_size_mb: int) -> bool`
Validate file size is within limits.

### `format_timestamp() -> str`
Return formatted timestamp string.