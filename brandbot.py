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
    generate_branding_snippet(user_input)

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_branding_snippet(prompt: str):
  
    enriched_prompt = f"Generate upbeat branding snippet for {prompt}: "

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": enriched_prompt}
        ],
        max_tokens=30
    )
    print(response)
    branding_text = response["choices"][0]["message"]["content"]
    print(branding_text)

if __name__ == "__main__":
    main()