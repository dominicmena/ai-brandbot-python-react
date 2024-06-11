import os
from typing import List
from dotenv import load_dotenv
import openai
import argparse
import re

import warnings
from urllib3.exceptions import NotOpenSSLWarning

# Load environment variables from a .env file
load_dotenv()

warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

MAX_INPUT_LENGTH = 12

def main():
    print("Running brandbot!")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    if validate_length(user_input):
        branding_result = generate_branding_snippet(user_input)
        keywords_result = generate_keywords(user_input)
        print(branding_result)
        print(keywords_result)

    else:
        raise ValueError(f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is {user_input}")


def validate_length(prompt: str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH


openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_keywords(prompt: str) -> List[str]:

    enriched_prompt = f"Generate related branding keywords for {prompt}: "

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
    keywords_text: str = response["choices"][0]["message"]["content"]

    # strip whitespace
    keywords_text = keywords_text.strip()
    keywords_array = re.split(r'\d+\.\s+|\n', keywords_text)
    keywords_array = [k.lower().strip() for k in keywords_array]
    keywords_array = [k for k in keywords_array if len(k) > 0]

    return keywords_array


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
