import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings


class Retriever:
    def __init__(self):
        load_dotenv()
        rag_path = os.environ['RAG_PATH']

        embedding_model = "BAAI/bge-base-en-v1.5"
        embeddings = HuggingFaceEmbeddings(model=embedding_model)

        index_name = os.environ['PINECONE_INDEX_NAME']
        vectorstore = PineconeVectorStore(
            index_name=index_name,
            embedding=embeddings
        )

        self.retriever = vectorstore.as_retriever(
            search_kwargs={
                "k": 5
            }
        )
