# Fitness Chatbot
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as gai

# Set the API key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# function to load the model
model = gai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


def get_response(question):
    response = chat.send_message(question, stream=True)
    return response


##initialize our streamlit app

st.set_page_config(page_title="Fitness Chatbot", page_icon="🤖", layout="centered")

st.header("Fitness Chatbot")

# Initialize session state for chat history if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_response(input)
    # Add user query and response to session state chat history
    st.session_state["chat_history"].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append(("Bot", chunk.text))
st.subheader("The Chat History is")

for role, text in st.session_state["chat_history"]:
    st.write(f"{role}: {text}")
