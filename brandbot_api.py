from typing import Union
from brandbot import generate_branding_snippet, generate_keywords

from fastapi import FastAPI

app = FastAPI()


@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
     snippet = generate_branding_snippet(prompt)
     return {"snippet": snippet}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# RUN SERVER: fastapi dev branbot_api.py