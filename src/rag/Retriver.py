import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


class Retriever:
    def __init__(self):
        load_dotenv()
        rag_path = os.environ['RAG_PATH']

        embedding_model = "BAAI/bge-base-en-v1.5"
        embeddings = HuggingFaceEmbeddings(model=embedding_model)

        vectorstore = FAISS.load_local(rag_path, embeddings, allow_dangerous_deserialization=True)
        self.retriever = vectorstore.as_retriever(
            search_type="similarity", 
            search_kwargs={
                "k": 5
            }
        )
