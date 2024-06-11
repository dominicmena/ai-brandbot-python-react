import os
from dotenv import load_dotenv
import openai

# Load environment variables from a .env file
load_dotenv()

# Get the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(engine="davinci", prompt="this is a test", max_tokens=5)
print(response)