import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    # Test API key by creating a simple chat completion request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, world!"}
        ]
    )
    # Print the response
    print(response['choices'][0]['message']['content'].strip())
except Exception as e:
    print(f"Error: {e}")
