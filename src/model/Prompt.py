from langchain_core.prompts import ChatPromptTemplate


class Prompt:
    def __init__(self):
        self.system_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system", 
                    "Responda de forma clara e objetiva às perguntas dos usuários."
                ),
                (
                    "human", 
                    "{input}"
                )
            ]
        )

    