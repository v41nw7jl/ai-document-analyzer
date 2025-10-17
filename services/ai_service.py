from groq import Groq
from config.settings import settings

class AIService:
    """Service for interacting with Groq API"""
    
    def __init__(self):
        """Initialize Groq client"""
        self.client = Groq(api_key=settings.GROQ_API_KEY)
    
    def analyze_text(self, text: str, question: str = None) -> str:
        """
        Analyze text using AI
        
        Args:
            text: The text content to analyze
            question: Optional specific question about the text
            
        Returns:
            AI's response as string
        """
        try:
            if question:
                prompt = f"""Here is a document:

<document>
{text}
</document>

Please answer this question about the document: {question}"""
            else:
                prompt = f"""Please analyze this document and provide:
1. A brief summary
2. Key points (3-5 bullet points)
3. Main topics covered

Document:
{text}"""
            
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=settings.GROQ_MODEL,
                max_tokens=settings.MAX_TOKENS,
            )
            
            return chat_completion.choices[0].message.content
            
        except Exception as e:
            raise Exception(f"Error calling AI API: {str(e)}")
    
    def summarize(self, text: str, length: str = "medium") -> str:
        """
        Summarize text
        
        Args:
            text: Text to summarize
            length: 'short', 'medium', or 'long'
            
        Returns:
            Summary text
        """
        length_instructions = {
            "short": "in 2-3 sentences",
            "medium": "in one paragraph (5-7 sentences)",
            "long": "in 2-3 paragraphs"
        }
        
        prompt = f"Please summarize the following text {length_instructions.get(length, 'concisely')}:\n\n{text}"
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=settings.GROQ_MODEL,
                max_tokens=settings.MAX_TOKENS,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error summarizing text: {str(e)}")