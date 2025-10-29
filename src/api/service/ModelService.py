from src.model.ModelChain import ModelChain
from src.model.Prompt import Prompt
from src.model.Model import Model
from src.api.model.AskModel import AskModel
from src.api.model.AIResponseModel import AIResponseModel
from src.rag.Retriver import Retriever


class ModelService:
    def __init__(self):
        prompt = Prompt().system_prompt
        model = Model().llm
        self.retriver = Retriever().retriever
        self.chain = ModelChain(prompt, model, self.retriver)
        self.chain = self.chain.chain


    def ask(self, question: AskModel):
        model_response = self.chain.invoke(question.question)
        print(model_response)
        answer = model_response.content
        # response_metadata = model_response.response_metadata # Will be used to monitoring
        return AIResponseModel(answer=answer)
        # return model_response

