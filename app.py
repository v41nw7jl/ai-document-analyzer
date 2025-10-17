import streamlit as st
from config.settings import settings
from services.ai_service import AIService
from utils.file_handler import FileHandler
from utils.helpers import validate_file_size, truncate_text

# Page configuration
st.set_page_config(
    page_title=settings.APP_NAME,
    page_icon="🤖",
    layout="wide"
)

# Initialize services
@st.cache_resource
def get_ai_service():
    return AIService()

def main():
    st.title("🤖 AI Document Analyzer")
    st.markdown("Upload a document and ask questions or get AI-powered analysis")
    
    # Validate settings
    try:
        settings.validate()
    except ValueError as e:
        st.error(f"Configuration Error: {str(e)}")
        st.info("Please set up your .env file with ANTHROPIC_API_KEY")
        st.stop()
    
    # Initialize session state
    if 'document_text' not in st.session_state:
        st.session_state.document_text = None
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Sidebar
    with st.sidebar:
        st.header("📁 Upload Document")
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=settings.SUPPORTED_FILE_TYPES,
            help=f"Max file size: {settings.MAX_FILE_SIZE_MB}MB"
        )
        
        if uploaded_file:
            try:
                # Debug info
                st.write(f"📊 File info: {uploaded_file.name}, Size: {uploaded_file.size / 1024:.2f} KB")
        
                # Validate file size
                if not validate_file_size(uploaded_file, settings.MAX_FILE_SIZE_MB):
                    st.error(f"File too large! Max size: {settings.MAX_FILE_SIZE_MB}MB")
                    st.stop()
            except Exception as e:
                st.error(f"Error reading file: {str(e)}")
                st.stop()
            
            # Process file
            with st.spinner("Processing document..."):
                try:
                    file_handler = FileHandler()
                    file_ext = file_handler.get_file_extension(uploaded_file.name)
                    
                    if file_ext == "pdf":
                        text = file_handler.extract_text_from_pdf(uploaded_file)
                    elif file_ext == "txt":
                        text = file_handler.extract_text_from_txt(uploaded_file)
                    else:
                        st.error("Unsupported file type")
                        st.stop()
                    
                    st.session_state.document_text = text
                    st.success("✅ Document loaded successfully!")
                    st.info(f"📄 {len(text)} characters extracted")
                    
                except Exception as e:
                    st.error(f"Error processing file: {str(e)}")
                    st.stop()
        
        st.divider()
        st.header("⚙️ Options")
        analysis_type = st.selectbox(
            "Analysis Type",
            ["Q&A", "Summary", "Key Points"]
        )
        
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()
    
    # Main content
    if st.session_state.document_text:
        
        # Display document preview
        with st.expander("📄 Document Preview"):
            st.text_area(
                "Content",
                truncate_text(st.session_state.document_text, 500),
                height=150,
                disabled=True
            )
        
        # Chat interface
        st.subheader("💬 Chat with your document")
        
        # Display chat history
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        
        # User input
        if prompt := st.chat_input("Ask a question about your document..."):
            # Add user message
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            
            with st.chat_message("user"):
                st.write(prompt)
            
            # Get Claude response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        ai_service = get_ai_service()
                        
                        if analysis_type == "Summary":
                            response = ai_service.summarize(
                                st.session_state.document_text
                            )
                        else:
                            response = ai_service.analyze_text(
                                st.session_state.document_text,
                                prompt if analysis_type == "Q&A" else None
                            )
                        
                        st.write(response)
                        st.session_state.chat_history.append(
                            {"role": "assistant", "content": response}
                        )
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
        
        # Quick actions
        st.divider()
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📝 Get Summary"):
                with st.spinner("Generating summary..."):
                    try:
                        ai_service = get_ai_service()
                        summary = ai_service.summarize(st.session_state.document_text)
                        st.session_state.chat_history.append(
                            {"role": "assistant", "content": f"**Summary:**\n\n{summary}"}
                        )
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
        
        with col2:
            if st.button("🎯 Extract Key Points"):
                with st.spinner("Extracting key points..."):
                    try:
                        ai_service = get_ai_service()
                        response = ai_service.analyze_text(
                            st.session_state.document_text,
                            "What are the key points in this document? List them as bullet points."
                        )
                        st.session_state.chat_history.append(
                            {"role": "assistant", "content": response}
                        )
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
        
        with col3:
            if st.button("📊 Generate Report"):
                with st.spinner("Generating report..."):
                    try:
                        ai_service = get_ai_service()
                        response = ai_service.analyze_text(st.session_state.document_text)
                        st.session_state.chat_history.append(
                            {"role": "assistant", "content": f"**Analysis Report:**\n\n{response}"}
                        )
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
    
    else:
        st.info("👈 Please upload a document to get started")
        
        # Show demo/instructions
        st.markdown("""
        ### How to use:
        1. Upload a PDF or TXT file using the sidebar
        2. Choose your analysis type
        3. Ask questions or use quick actions
        4. Get AI-powered insights instantly
        
        ### Features:
        - 📄 Document analysis
        - 💬 Interactive Q&A
        - 📝 Summarization
        - 🎯 Key point extraction
        """)

if __name__ == "__main__":
    main()