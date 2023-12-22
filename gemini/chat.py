from dotenv import load_dotenv

load_dotenv()  # load all the environment variables

import streamlit as st

import os

import json

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# function to load gemini model and gemini pro model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


def get_gemini_response(question):
    response = chat.send_message(question)

    return response.text


@st.cache_data
def load_chat_history():
    try:
        with open("chat_history.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Function to save chat history to a file
def save_chat_history(chat_history):
    with open("chat_history.json", "w") as file:
        json.dump(chat_history, file)


st.set_page_config(page_title="Chat Conversation Demo")
st.header("Gemini Chat Application")

chats_history = load_chat_history()

for chats in chats_history:
    st.text(chats)

user_input = st.text_input("Enter your message:")
if st.button("Send"):
    # Display user's message and add it to chat history
    st.text(f"You: {user_input}")
    chats_history.append(f"You: {user_input}")

    # Send the message to Gemini API and display the response
    api_response = get_gemini_response(user_input)
    st.text(f"Gemini API: {api_response}")
    chats_history.append(f"Gemini API: {api_response}")

    save_chat_history(chats_history)
