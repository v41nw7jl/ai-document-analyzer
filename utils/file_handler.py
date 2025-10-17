import PyPDF2
from io import BytesIO
from typing import Optional

class FileHandler:
    """Handle file operations"""
    
    @staticmethod
    def extract_text_from_pdf(file) -> str:
        """
        Extract text from PDF file
        
        Args:
            file: Uploaded file object
            
        Returns:
            Extracted text as string
        """
        try:
            pdf_reader = PyPDF2.PdfReader(BytesIO(file.read()))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            raise Exception(f"Error reading PDF: {str(e)}")
    
    @staticmethod
    def extract_text_from_txt(file) -> str:
        """
        Extract text from TXT file
        
        Args:
            file: Uploaded file object
            
        Returns:
            Text content as string
        """
        try:
            return file.read().decode('utf-8')
        except Exception as e:
            raise Exception(f"Error reading text file: {str(e)}")
    
    @staticmethod
    def get_file_extension(filename: str) -> Optional[str]:
        """Get file extension from filename"""
        return filename.split('.')[-1].lower() if '.' in filename else None