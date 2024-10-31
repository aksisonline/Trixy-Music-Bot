import streamlit as st
from sentence_transformers import SentenceTransformer
import requests
from googlesearch import search
import json
import syncedlyrics
import re


# Set your API key and base URL
api_key = 'ollama'
api_base = 'http://localhost:11434/v1'

def chat_with_api(prompt, google_results):
    url = f"{api_base}/chat/completions"
    headers = { 
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gemma2:2b',
        'messages': [
            {
                'role': 'system',
                'content': 'Your name is Trixy and you are a music chatbot. You are here to help me with music-related questions. When asked for lyrics mentioning song name and artist name, respond with the song name and artist in the format: "Song: [song name], Artist: [artist name]". Else, answer any normal question as a normal query with the information that you know.'
            },
            {
                'role': 'user',
                'content': f"{prompt}\n\nGoogle search results:\n{google_results}"
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    return response_json['choices'][0]['message']['content'].strip()

def search_google(query):
    try:
        search_results = search(query, num_results=10)
        results = []
        
        for result in search_results:
            results.append(result)

        return "\n\n".join(results)  # Return top 3 results
    except Exception as e:
        print(f"Error searching Google: {e}")
        return "Could not fetch Google results."

def get_lyrics(artist, song):
    try:
        lyrics = syncedlyrics.search(f"{song} {artist}")
        # Use regex to remove timestamps and format lyrics
        lyrics = re.sub(r'\[\d{2}:\d{2}\.\d{2}\]', '\n', lyrics)
        lyrics = lyrics.strip()
        return lyrics
    except Exception as e:
        print(f"Error fetching lyrics: {e}")
        return "Could not fetch lyrics."

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit app
st.title("Trixy Music Bot")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("You: "):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Perform Google search
    google_results = search_google(prompt)

    # Get response from the API
    bot_response = chat_with_api(prompt, google_results)
    
    # Check if the bot response contains a request for lyrics
    if "song:" in bot_response.lower() and "artist:" in bot_response.lower():
        # Extract artist and song name from the bot response
        try:
            song = bot_response.split("Song:")[1].split(",")[0].strip()
            artist = bot_response.split("Artist:")[1].strip()
            lyrics = get_lyrics(artist, song)
            bot_response = f"Sure, here are the lyrics for '{song}' by {artist}:\n\n{lyrics}"
        except Exception as e:
            bot_response = "Sorry, I couldn't understand the song and artist name."

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})