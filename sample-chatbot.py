import requests
import json

# Set your API key and base URL
api_key = 'ollama'
api_base = 'http://localhost:11434/v1'

def chat_with_api(prompt):
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
                'content': 'Your name is Trixy and you are a music chatbot. You are here to help me with music-related questions. '
            },
            {
                'role': 'user',
                'content': prompt
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    return response_json['choices'][0]['message']['content'].strip()

def main():
    print("Welcome to the OpenAI Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = chat_with_api(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()