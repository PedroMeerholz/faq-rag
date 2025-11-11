import os
from dotenv import load_dotenv
from fastapi import UploadFile
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


class RagService:
    def __init__(self):
        load_dotenv()

        self.documents_path = os.environ['DOCUMENTS_PATH']
        self.rag_path = os.environ['RAG_PATH']

        embedding_model = os.environ['EMBEDDING_MODEL']
        self.embeddings = HuggingFaceEmbeddings(model=embedding_model)

        self.chunck_size = 1000
    

    async def add_document(self, document: UploadFile):
        try:
            file_name = f"{self.documents_path}/{document.filename}" 
            with open(file_name, "wb") as new_file:
                content = await document.read()
                new_file.write(content)

            loader = PyPDFLoader(file_name)
            new_document = loader.load()

            text_splitter = CharacterTextSplitter(
                chunk_size=self.chunck_size, 
                chunk_overlap=self.chunck_size*0.15
            )
            new_document = text_splitter.split_documents(new_document)

            index_name = os.environ['PINECONE_INDEX_NAME']
            vectorstore = PineconeVectorStore(
                index_name=index_name,
                embedding=self.embeddings
            )

            vectorstore.add_documents(new_document)
        except Exception as e:
            return {"error": str(e)}
