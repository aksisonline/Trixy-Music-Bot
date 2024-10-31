# Trixy Music Bot

Trixy is a music chatbot designed to help users with music-related questions. It can search for information on Google, fetch song lyrics, and provide responses based on the user's queries. Trixy uses an OpenAI-compatible API as its LLM interface to generate responses.

## Features

- **Google Search Integration**: Trixy can search Google for information and include the results in its responses.
- **Lyrics Fetching**: Trixy can fetch lyrics for a given song and artist.
- **Interactive Chat**: Users can interact with Trixy through a chat interface.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/trixy-music-bot.git
   cd trixy-music-bot
   ```
2. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Start the Streamlit app:

   ```sh
   streamlit run main.py
   ```
2. Open your web browser and go to `http://localhost:8501` to interact with Trixy.

## Files

### `main.py`

- `chat_with_api(prompt, google_results)`: Sends a prompt and Google search results to the chatbot API and returns the response.
- `search_google(query)`: Searches Google for the given query and returns the top 10 results.
- `get_lyrics(artist, song)`: Fetches lyrics for the given song and artist.

### `sample-chatbot.py`

- `chat_with_api(prompt)`: Sends a prompt to the chatbot API and returns the response.
- `main()`: The main function that runs the sample chatbot script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
