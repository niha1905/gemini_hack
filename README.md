# Gemini Hack 🤖

## Overview

Gemini Hack is an AI-powered conversational application that integrates Google's Gemini 1.5 Flash model with both Flask web framework and Streamlit interfaces. The project provides multiple interaction modes including a web dashboard, chatbot interface, and Q&A system for intelligent conversations and predictions.

## 🚀 Key Features

### AI Chat Interfaces
- **Streamlit Chat Interface** - Interactive Q&A with chat history tracking
- **Flask Chatbot API** - RESTful endpoint for chatbot interactions
- **Dashboard Interface** - Web-based dashboard for monitoring and interaction
- **Gemini Integration** - Powered by Google Gemini 1.5 Flash model with streaming responses

### Prediction System
- **Occupancy Prediction** - Predict occupancy based on date, season, and holiday parameters
- **Form-based Input** - User-friendly form interface for predictions

### Dual Framework Support
- **Flask Backend** - Lightweight REST API with multiple routes
- **Streamlit UI** - Modern, responsive chat interface with real-time streaming

## 📁 Project Structure

```
gemini_hack/
├── app.py              # Main Flask application with routes
├── chatbot.py          # Streamlit chatbot interface
├── qachat.py           # Q&A chat functionality
├── config.py           # Configuration settings
├── dashboard.html      # Dashboard interface
└── index.html          # Main landing page
```

## 🛠️ Tech Stack

**Backend Framework:**
- Flask - Web server and routing
- Python 3.8+

**AI/ML:**
- Google Generative AI (Gemini 1.5 Flash)
- Streaming responses for real-time interaction

**Frontend:**
- Streamlit - Interactive UI components
- HTML/CSS/JavaScript - Dashboard and landing pages

**Dependencies:**
- `google-generativeai` - Gemini AI SDK
- `streamlit` - UI framework
- `flask` - Web framework
- `python-dotenv` - Environment variable management

## 🔧 Installation

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key from [Google AI Studio](https://makersuite.google.com/)
- pip package manager

### Setup Steps

1. **Clone the repository:**
```bash
git clone https://github.com/niha1905/gemini_hack.git
cd gemini_hack
```

2. **Install dependencies:**
```bash
pip install flask google-generativeai streamlit python-dotenv
```

3. **Configure environment variables:**

Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

Or set the API key in the configuration files.

4. **Run Flask application:**
```bash
python app.py
```

5. **Run Streamlit chatbot (in separate terminal):**
```bash
streamlit run chatbot.py
```
or
```bash
streamlit run qachat.py
```

## 📡 API Endpoints

### Flask Routes

#### GET `/`
- **Description:** Dashboard homepage
- **Returns:** `dashboard.html` interface

#### POST `/chatbot`
- **Description:** Chatbot API endpoint
- **Request Body:**
  ```json
  {
    "message": "your message here"
  }
  ```
- **Response:**
  ```json
  {
    "response": "bot response"
  }
  ```

#### POST `/predict`
- **Description:** Occupancy prediction endpoint
- **Request Body (form data):**
  - `date` - Date for prediction
  - `season` - Season information
  - `holiday` - Holiday indicator
- **Response:**
  ```json
  {
    "occupancy": prediction_value
  }
  ```

#### GET `/gemini`
- **Description:** Streamlit Gemini chat interface
- **Returns:** Embedded Streamlit app with chat history

## 💻 Usage

### Flask Dashboard

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Access different features:
   - Dashboard: `http://localhost:5000/`
   - Chatbot API: POST to `http://localhost:5000/chatbot`
   - Predictions: POST to `http://localhost:5000/predict`

### Streamlit Chat Interfaces

#### Option 1: Q&A Chat (qachat.py)
```bash
streamlit run qachat.py
```
- Opens on `http://localhost:8501`
- Features chat history tracking
- Streaming responses from Gemini

#### Option 2: Chatbot Interface (chatbot.py)
```bash
streamlit run chatbot.py
```
- Opens on `http://localhost:8501`
- Similar Q&A functionality with alternate styling

### Using the Chat Interface

1. Enter your question in the input field
2. Click "Ask question" button
3. View streaming response in real-time
4. Check chat history below to see conversation context
5. Continue asking follow-up questions

## 🎯 Features in Detail

### Gemini AI Integration
- Model: `gemini-1.5-flash`
- Chat history management for context-aware conversations
- Streaming responses for real-time user feedback
- Session state management in Streamlit

### Dashboard Features
- Interactive HTML interface
- Real-time monitoring capabilities
- Integrated with Flask backend

### Prediction System
- Form-based occupancy prediction
- Configurable parameters (date, season, holiday)
- REST API for integration

## 🔐 Configuration

The application uses environment variables for API key management. Configure your API key in:

1. `.env` file (recommended)
2. `config.py` file
3. Directly in the code (not recommended for production)

## 📝 Notes

- The application uses Google Gemini 1.5 Flash model for AI responses
- Chat history is maintained during the session
- Streaming responses provide real-time feedback
- Multiple deployment options (Flask, Streamlit)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

MIT License

## 👤 Author

**Nihaarika S**

Department of Computer Science and Engineering  
SRM Institute of Science and Technology, Chennai, India

📧 [ns1490@srmist.edu.in](mailto:ns1490@srmist.edu.in)  
🌐 [LinkedIn](https://www.linkedin.com/in/nihaarika-s-23033a259/)

## 🙏 Acknowledgments

- **Google Gemini AI** - For providing the powerful AI model
- **Flask Community** - For the excellent web framework
- **Streamlit** - For the interactive UI framework
- **Hackathon Organizers** - For the opportunity to develop this project
