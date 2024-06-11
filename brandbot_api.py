from typing import Union
from brandbot import generate_branding_snippet, generate_keywords

from fastapi import FastAPI

app = FastAPI()


@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
     snippet = generate_branding_snippet(prompt)
     return {"snippet": snippet, "keywords": []}


@app.get("/generate_keywords")
async def generate_keywords_api(prompt: str):
     keywords = generate_keywords(prompt)
     return {"snippet": None, "keywords": keywords}

@app.get("/generate_snippet_and_keywords")
async def generate_keywords_api(prompt: str):
     snippet = generate_branding_snippet(prompt)
     keywords = generate_keywords(prompt)
     return {"snippet": snippet, "keywords": keywords}

# RUN SERVER: fastapi dev branbot_api.py /// http://127.0.0.1:8000/docs for dashboard