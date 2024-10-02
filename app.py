from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st

# Load environment variables
load_dotenv()

# Configure generative AI API
api_key = os.getenv("AIzaSyBjfnEfZ-y5nbVgSo2iopR6mNC5G7ptNQk")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

app = Flask(__name__)

# Route for the dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# API endpoint for chatbot in Flask
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    # Simple bot response logic
    if user_message.lower() == 'hello':
        response = 'Hello! How can I assist you today?'
    else:
        response = 'Sorry, I can’t understand. Please try again.'
    return jsonify({'response': response})

# API endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    date = request.form['date']
    season = request.form['season']
    holiday = request.form['holiday']
    # Call the prediction model (dummy function for now)
    
    prediction = predict_occupancy(date, season, holiday)
    return jsonify({'occupancy': prediction})

# Route to serve the Streamlit Gemini chat model interface
@app.route('/gemini')
def gemini():
    st.set_page_config(page_title="Q&A Demo", layout="wide")

    def get_gemini_response(question):
        response = chat.send_message(question, stream=True)
        return response

    # Streamlit code
    st.markdown(
        """
        <style>
        .centered-heading {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="centered-heading">Gemini Chat Model</h1>', unsafe_allow_html=True)

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    input_text = st.text_input("Input:", key="input")
    submit = st.button("Ask question")

    if submit and input_text:
        response = get_gemini_response(input_text)

        # Append user input to the session state
        st.session_state['chat_history'].append(("You", input_text))

        st.subheader("The Response")
        bot_response = ""
        for chunk in response:
            bot_response += chunk.text
        st.session_state['chat_history'].append(("Bot", bot_response))
        st.write(bot_response)

    st.subheader("The Chat history is:")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")

    return "Streamlit app running"


if __name__ == '__main__':
    app.run(debug=True)