import streamlit as st
import os
import google.generativeai as genai

# Load the environment variables
api_key = os.getenv('GOOGLE_API_KEY')  # Ensure you have your API key set in the environment
genai.configure(api_key=api_key)

st.set_page_config(page_title="Q&A Demo", layout="wide")

# Set up the chat model
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

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
    # Get response from the Google Generative AI model
    response = chat.send_message(input_text, stream=True)
    
    # Construct the bot's response
    bot_response = ""
    for chunk in response:
        bot_response += chunk.text
    
    # Append user input and bot response to chat history
    st.session_state['chat_history'].append(("You", input_text))
    st.session_state['chat_history'].append(("Bot", bot_response))
    
    st.subheader("The Response")
    st.write(bot_response)

st.subheader("The Chat history is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
