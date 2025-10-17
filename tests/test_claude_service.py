import pytest
from services.claude_service import ClaudeService
from config.settings import settings

def test_claude_service_initialization():
    """Test Claude service can be initialized"""
    service = ClaudeService()
    assert service.client is not None

def test_analyze_text_with_question():
    """Test text analysis with specific question"""
    service = ClaudeService()
    text = "The quick brown fox jumps over the lazy dog."
    question = "What animal is mentioned?"
    
    # This test requires valid API key
    if settings.ANTHROPIC_API_KEY:
        response = service.analyze_text(text, question)
        assert isinstance(response, str)
        assert len(response) > 0

# Add more tests as needed