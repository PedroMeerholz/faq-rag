import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


load_dotenv()
docs_path = os.environ['DOCUMENTS_PATH']
rag_path = os.environ['RAG_PATH']
embedding_model = os.environ['EMBEDDING_MODEL']
index_name = os.environ['PINECONE_INDEX_NAME']

embeddings = HuggingFaceEmbeddings(model=embedding_model)

loader = DirectoryLoader(docs_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
documents = loader.load()

chunck_size = 1000
text_splitter = CharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=chunck_size*0.15
)
documents = text_splitter.split_documents(documents)

vectorstore = PineconeVectorStore.from_documents(
    documents=documents,
    embedding=embeddings,
    index_name=index_name
)
