# System Architecture

## Overview

AI Document Analyzer is built using a modular architecture with clear separation of concerns.

## Architecture Diagram
```
┌─────────────────────────────────────────┐
│           Streamlit UI Layer            │
│         (app.py - Frontend)             │
└──────────────┬──────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────┐
│        Application Services              │
│  ┌────────────────────────────────────┐  │
│  │   ClaudeService (Claude API)       │  │
│  └────────────────────────────────────┘  │
│  ┌────────────────────────────────────┐  │
│  │   FileHandler (Document Processing)│  │
│  └────────────────────────────────────┘  │
└──────────────┬───────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────┐
│          External Services               │
│  ┌────────────────────────────────────┐  │
│  │      Anthropic Claude API          │  │
│  └────────────────────────────────────┘  │
└──────────────────────────────────────────┘
```

## Components

### 1. Presentation Layer (app.py)
- Streamlit-based user interface
- File upload handling
- Chat interface
- Quick action buttons
- Session state management

### 2. Service Layer
#### ClaudeService
- Manages Claude API interactions
- Handles different analysis types
- Error handling and retries
- Response formatting

#### FileHandler
- PDF text extraction
- TXT file processing
- File validation
- Format conversion

### 3. Configuration Layer
- Environment variable management
- Application settings
- API configuration
- Constants and defaults

### 4. Utility Layer
- Helper functions
- Common operations
- Validation utilities
- Formatting functions

## Data Flow

1. **User uploads document** → FileHandler extracts text
2. **Text stored in session state** → Available for all operations
3. **User asks question** → Sent to ClaudeService
4. **ClaudeService calls API** → Returns AI response
5. **Response displayed** → Added to chat history

## Security Considerations

- API keys stored in environment variables
- No sensitive data in code
- File size validation
- Input sanitization
- Error messages don't expose internals

## Scalability Considerations

- Stateless service design
- Caching for API client
- Session-based state management
- Modular architecture for easy extension

## Future Enhancements

- Database integration for history
- User authentication
- Multiple document support
- Export functionality
- Advanced analytics