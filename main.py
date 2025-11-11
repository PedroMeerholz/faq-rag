from fastapi import FastAPI, UploadFile

from src.api.model.AskModel import AskModel
from src.api.service.ModelService import ModelService
from src.api.service.RagService import RagService


app = FastAPI()
model_service = ModelService()
rag_service = RagService()


@app.post("/ask")
def ask(question: AskModel):
    return model_service.ask(question)


@app.post("/documents/add", status_code=201)
async def add_document(document: UploadFile):
    return await rag_service.add_document(document)
