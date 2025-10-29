from langchain_core.runnables import RunnablePassthrough, RunnableParallel


class ModelChain:
    def __init__(self, prompt, llm, retriever):
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        setup_and_retrieval = RunnableParallel(
            context=retriever | format_docs,
            question=RunnablePassthrough()
        )

        self.chain = (
            setup_and_retrieval
            | prompt
            | llm
        )

    