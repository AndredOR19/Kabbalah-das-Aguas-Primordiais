# main.py - FastAPI para SCII
from fastapi import FastAPI
from scripts.scii_core import translate

app = FastAPI(title="SCII API", description="Oráculo das Águas Primordiais", version="0.1")

@app.get("/scii/{word}")
def get_scii(word: str):
    return translate(word)
