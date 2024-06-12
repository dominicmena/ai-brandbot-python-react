from typing import Union
from brandbot import generate_branding_snippet, generate_keywords
from mangum import Mangum
from fastapi import FastAPI, HTTPException

app = FastAPI()
handler = Mangum(app)
MAX_INPUT_LENGTH = 32


@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []}


@app.get("/generate_keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": None, "keywords": keywords}


@app.get("/generate_snippet_and_keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}


def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400, detail=f"Input length is too long. must be under {MAX_INPUT_LENGTH} characters")


# RUN SERVER: fastapi dev branbot_api.py /// http://127.0.0.1:8000/docs for dashboard
