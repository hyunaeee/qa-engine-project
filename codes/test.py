import os
# from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
# from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

api_key = os.environ["OPENAI_API_KEY"]

# Load Document
# loader = TextLoader("../dataset/광주지법 2000. 5. 19. 선고 2000노24 판결 _ 상고기각.pdf") # TextLoader 
loader = DirectoryLoader("../dataset/판례", glob="*", show_progress=True)
docs = loader.load()
print(f"docs len : {len(docs)}")

# SemanticChunker
# text_splitter = SemanticChunker(OpenAIEmbeddings(api_key=api_key))
# documents = text_splitter.split_documents(docs)
# print(f"documents len : {len(documents)}")

# RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " "],
    chunk_size=200,
    chunk_overlap=10,
    length_function=len,
    is_separator_regex=False
)
documents = text_splitter.split_documents(docs)
print(f"documents len : {len(documents)}")
# print(documents[0])


# Embedding / FAISS VectorStore / vector index save
embed_model = OpenAIEmbeddings(api_key=api_key,
                               model="text-embedding-3-small")
vector_index = FAISS.from_documents(documents, embed_model)
# vector_index.save_local("../models/faiss_medical_law.json") # SemanticChunker
vector_index.save_local("../models/faiss_medical_law_rec.json") # RecursiveCharacterTextSplitter


