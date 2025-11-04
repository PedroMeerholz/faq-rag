import os
from dotenv import load_dotenv
from fastapi import UploadFile
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


class RagService:
    def __init__(self):
        load_dotenv()

        self.documents_path = os.environ['DOCUMENTS_PATH']
        self.rag_path = os.environ['RAG_PATH']

        embedding_model = os.environ['EMBEDDING_MODEL']
        self.embeddings = HuggingFaceEmbeddings(model=embedding_model)
    

    async def add_document(self, document: UploadFile):
        try:
            file_name = f"{self.documents_path}/{document.filename}" 
            with open(file_name, "wb") as new_file:
                content = await document.read()
                new_file.write(content)

            loader = DirectoryLoader(self.documents_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
            documents = loader.load()

            chunck_size = 1000
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=chunck_size*0.15)
            documents = text_splitter.split_documents(documents)

            vectorstore = FAISS.from_documents(documents, self.embeddings)
            vectorstore.save_local(self.rag_path)
        except Exception as e:
            return {"error": str(e)}
