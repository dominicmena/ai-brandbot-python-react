import os
from dotenv import load_dotenv
import openai
import argparse

import warnings
from urllib3.exceptions import NotOpenSSLWarning

# Load environment variables from a .env file
load_dotenv()

warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

def main():
    print("Running brandbot!")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    pass

# # Get the API key from the environment variable
# openai.api_key = os.getenv("OPENAI_API_KEY")

# subject = "coffee"
# prompt = f"Generate upbeat branding snippet for {subject}"

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": prompt}
#     ],
#     max_tokens=30
# )
# print(response)

if __name__ == "__main__":
    main()