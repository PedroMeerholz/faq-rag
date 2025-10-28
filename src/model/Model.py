import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from src.model.Prompt import Prompt


class Model:
    def __init__(self):
        load_dotenv()
        self.llm = ChatGroq(
            api_key=os.environ['GROQ_CLOUD_API_KEY'],
            model = os.environ['MODEL_NAME'],
            temperature=0,
            max_retries=3,
        )
