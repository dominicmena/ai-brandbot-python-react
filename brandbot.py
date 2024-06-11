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
    result = generate_branding_snippet(user_input)
    print(result)
 

openai.api_key = os.getenv("OPENAI_API_KEY") 

def generate_branding_snippet(prompt: str) -> str:
  
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

    # extract output text
    branding_text: str = response["choices"][0]["message"]["content"]

    # strip whitespace
    branding_text = branding_text.strip()
    last_char = branding_text[-1]

# add elipses
    if last_char not in {".", "!", "?"}:
        branding_text += "..."

    return branding_text

if __name__ == "__main__":
    main()