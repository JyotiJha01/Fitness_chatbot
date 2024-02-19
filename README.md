# Fitness Chatbot using Gemini Pro

This is a Fitness Chatbot built using Streamlit and Google's Gemini Pro model. The chatbot assists users in generating personalized workout plans based on their body type, fitness goals, and any dietary restrictions they may have.


## Features:
**Personalized Workout Plans**: Users can select their body type (Slim, Average, Stocky), describe their fitness goals, and optionally specify any dietary restrictions. The chatbot then generates a personalized workout plan tailored to the user's inputs.

**Interactive Chat Interface**: The chatbot provides an interactive chat interface where users can ask questions related to fitness, nutrition, or any other relevant topics. The chat history is displayed for reference.

**Integration with Gemini Pro**: The chatbot leverages Google's Gemini Pro model to provide intelligent responses to user queries, ensuring a seamless and engaging user experience.

## How to Use:

**Select Body Type**: Choose your body type from the dropdown menu (Slim, Average, Stocky).

**Describe Fitness Goals**: Describe your fitness goals in the text area provided.

**Specify Dietary Restrictions**: Optionally, specify any dietary restrictions you may have in the text area.

**Generate Workout Plan**: Click the "Generate Workout Plan" button to receive a personalized workout plan based on your inputs.

**Ask Questions**: Use the text input field to ask questions related to fitness or any other topics. Click the "Ask the question" button to get responses from the chatbot.

**View Chat History**: The chat history is displayed below the input fields, showing the interaction between the user and the chatbot.

## Installation:
To run the Fitness Chatbot locally, follow these steps:

1. Clone the repository:

    *git clone git@github.com:JyotiJha01/Fitness_chatbot.git*

2. Create a virtual environment: 

    *conda create -n env*

3. Activate the virtual environment: 
    
    *conda activate env*

4. Install dependencies:

    *pip install -r requirements.txt*

5. Set up Google API key: Obtain a Google API key and set it in the .env file:

    *GOOGLE_API_KEY=your_google_api_key*

6. Run the Streamlit app:

    *streamlit run app.py*

[Watch the Video](https://youtu.be/-ghTEN_cV0g?si=JX3Niz9oBncyIPHg)


## Deployment:
The Fitness Chatbot can be deployed using various platforms such as Streamlit Sharing, Heroku, or Docker. 

Follow the deployment instructions provided by the chosen platform to deploy the application.

## Technologies Used:

Streamlit: For building the interactive web application.

Google's Gemini Pro: For integrating the chatbot with advanced natural language processing capabilities.

Python: For backend logic and scripting.

dotenv: For managing environment variables.