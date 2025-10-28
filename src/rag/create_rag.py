import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


load_dotenv()
docs_path = os.environ['DOCUMENTS_PATH']
rag_path = os.environ['RAG_PATH']

embedding_model = "BAAI/bge-base-en-v1.5"
embeddings = HuggingFaceEmbeddings(model=embedding_model)

loader = DirectoryLoader(docs_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
documents = loader.load()

chunck_size = 1000
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=chunck_size*0.15)
documents = text_splitter.split_documents(documents)

vectorstore = FAISS.from_documents(documents, embeddings)
vectorstore.save_local(rag_path)
