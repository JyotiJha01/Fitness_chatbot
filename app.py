# Fitness Chatbot using Gemini Pro

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

import os
import google.generativeai as gai


# Define function to generate workout plan based on user inputs
def generate_workout_plan(body_type, fitness_goals, dietary_restrictions):
    # This is a placeholder function that generates a generic workout plan
    workout_plan = f"Your personalized workout plan:\n\nBody Type: {body_type}\nFitness Goals: {fitness_goals}\nDietary Restrictions: {dietary_restrictions}\n\nDay 1: Chest and Triceps\nDay 2: Back and Biceps\nDay 3: Rest\nDay 4: Legs\nDay 5: Shoulders and Abs\nDay 6: Rest\nDay 7: Rest"
    return workout_plan


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

# Collect user inputs for workout plan
body_type = st.selectbox(
    "Select your body type:", ["Slim", "Average", "Stocky"]
)
fitness_goals = st.text_area("Describe your fitness goals:")
dietary_restrictions = st.text_area("Any dietary restrictions (optional):")

# Generate workout plan based on user inputs
if st.button("Generate Workout Plan"):
    workout_plan = generate_workout_plan(body_type, fitness_goals, dietary_restrictions)
    st.subheader("Your Personalized Workout Plan:")
    st.write(workout_plan)
    st.session_state["chat_history"].append(("Bot", workout_plan))


# Collect user inputs for chatbot
input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Ask the question")

if submit_button and input_text:
    response = get_response(input_text)
    # Add user query and response to session state chat history
    st.session_state["chat_history"].append(("You", input_text))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append(("Bot", chunk.text))

st.subheader("The Chat History is")

for role, text in st.session_state["chat_history"]:
    st.write(f"{role}: {text}")


