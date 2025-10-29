import os
from dotenv import load_dotenv


load_dotenv()
rag_path = os.environ['RAG_PATH']
documents_path = os.environ['DOCUMENTS_PATH']

os.makedirs(rag_path, exist_ok=True)
os.makedirs(documents_path, exist_ok=True)