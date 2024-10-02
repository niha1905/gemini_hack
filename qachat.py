from dotenv import load_dotenv
load_dotenv()
import streamlit as st 
import os 
import google.generativeai as genai
st.set_page_config(page_title="Q&A Demo", layout="wide")
api_key = "AIzaSyBjfnEfZ-y5nbVgSo2iopR6mNC5G7ptNQk"  # Temporarily hardcoded for testing
genai.configure(api_key=api_key)

model= genai.GenerativeModel("gemini-1.5-flash")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question,stream=True)
    return response
st.markdown(
        """
        <style>
        .centered-heading {
            text-align: center; /* Center the text */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Use the custom class for the heading
st.markdown('<h1 class="centered-heading">Gemini Chat Model</h1>', unsafe_allow_html=True)


if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input:",key= "input")
submit = st.button("Ask question")

if submit and input:
    response = get_gemini_response(input)
    
    # Append user input as a tuple
    st.session_state['chat_history'].append(("You", input))
    
    st.subheader("The Response")
    bot_response = ""
    for chunk in response:
        bot_response += chunk.text  
    st.session_state['chat_history'].append(("Bot", bot_response))
    st.write(bot_response)
st.subheader("The Chat history is")
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
