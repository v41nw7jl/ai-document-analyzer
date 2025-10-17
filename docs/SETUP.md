# Setup Guide

## Local Development Setup

### 1. Prerequisites
- Python 3.8+
- Git
- Anthropic API Key

### 2. Installation Steps
```bash
# Clone repository
git clone https://github.com/yourusername/ai-document-analyzer.git
cd ai-document-analyzer

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env file and add your API key
```

### 3. Get Anthropic API Key

1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create new key
5. Copy and paste into .env file

### 4. Run Application
```bash
streamlit run app.py
```

Visit `http://localhost:8501`

## Deployment to Streamlit Cloud

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/ai-document-analyzer.git
git push -u origin main
```

### 2. Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Connect GitHub repository
4. Select branch: `main`
5. Main file path: `app.py`
6. Click "Advanced settings"
7. Add secrets:
```toml
ANTHROPIC_API_KEY = "your-api-key-here"
```
8. Click "Deploy"

## Troubleshooting

### API Key Issues
- Ensure .env file exists and contains valid key
- Check key has no extra spaces
- Verify key is active in Anthropic console

### File Upload Issues
- Check file size limits
- Ensure supported file types
- Verify file isn't corrupted

### Module Import Errors
```bash
pip install --upgrade -r requirements.txt
```