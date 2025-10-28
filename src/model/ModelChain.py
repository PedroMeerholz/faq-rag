class ModelChain:
    def __init__(self, prompt, llm):
        self.chain = prompt | llm
    