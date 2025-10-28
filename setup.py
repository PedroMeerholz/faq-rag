import os
from dotenv import load_dotenv


load_dotenv()

rag_path = os.environ['RAG_PATH']
os.makedirs(rag_path, exist_ok=True)
