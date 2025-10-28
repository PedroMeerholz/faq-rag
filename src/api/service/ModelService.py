from src.model.ModelChain import ModelChain
from src.model.Prompt import Prompt
from src.model.Model import Model
from src.api.model.AskModel import AskModel
from src.api.model.AIResponseModel import AIResponseModel


class ModelService:
    def __init__(self):
        prompt = Prompt()
        prompt = prompt.system_prompt
        model = Model()
        llm = model.llm
        self.chain = ModelChain(prompt, llm)


    def ask(self, question: AskModel):
        model_response = self.chain.chain.invoke({"input": question.question})
        answer = model_response.content
        # response_metadata = model_response.response_metadata # Will be used to monitoring
        return AIResponseModel(answer=answer)

