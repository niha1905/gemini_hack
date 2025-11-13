# Gemini Hack

## Overview
Gemini Hack is a web-based AI chatbot application built with Python Flask and integrated with Google's Gemini AI. The project features an interactive dashboard and intelligent conversational interface for enhanced user interactions.

## Project Structure

```
gemini_hack/
├── app.py           # Main Flask application
├── chatbot.py       # Chatbot logic and AI integration
├── config.py        # Configuration settings
├── qachat.py        # Q&A functionality
├── dashboard.html   # Dashboard interface
└── index.html       # Main landing page
```

## Tech Stack

- **Backend**: Python Flask
- **AI/ML**: Google Gemini AI API
- **Frontend**: HTML, CSS, JavaScript
- **Language Distribution**: 
  - HTML: 77.3%
  - Python: 22.7%

## Features

- 🤖 **AI-Powered Chatbot** - Intelligent conversations using Google Gemini
- 📊 **Interactive Dashboard** - User-friendly interface for interaction monitoring
- 💬 **Q&A System** - Question-answering functionality
- 🔧 **Configurable Settings** - Easy configuration management
- 🚀 **Flask Backend** - Lightweight and scalable Python web server

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/niha1905/gemini_hack.git
cd gemini_hack
```

2. Install dependencies:
```bash
pip install flask google-generativeai
```

3. Configure API key in `config.py`:
```python
GEMINI_API_KEY = "your-api-key-here"
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Access the main interface through `index.html`
2. Navigate to the dashboard to view interaction analytics
3. Use the chatbot interface for AI-powered conversations
4. Leverage the Q&A system for specific queries

## API Integration

This project uses the Google Gemini AI API for natural language processing and conversation generation. Make sure to obtain an API key from Google AI Studio.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

MIT License

## Author

**Nihaarika S**  
Department of Computer Science and Engineering  
SRM Institute of Science and Technology, Chennai, India  
📧 ns1490@srmist.edu.in  
🌐 [LinkedIn](https://www.linkedin.com/in/nihaarika-s-23033a259/)

## Acknowledgments

- Google Gemini AI for providing the AI capabilities
- Flask community for the excellent web framework
- Hackathon organizers for the opportunity to develop this project
