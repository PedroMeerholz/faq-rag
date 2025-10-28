from fastapi import FastAPI

from src.api.model.AskModel import AskModel
from src.api.service.ModelService import ModelService


app = FastAPI()
model_service = ModelService()


@app.post("/ask")
def ask(question: AskModel):
    return model_service.ask(question)
