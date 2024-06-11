import os
from dotenv import load_dotenv
import openai

# Load environment variables from a .env file
load_dotenv()

# Get the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "this is a test"}
    ],
    max_tokens=5
)
print(response)