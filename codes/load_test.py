import os
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

os.environ["OPENAI_API_KEY"]

embed_model = OpenAIEmbeddings(api_key=api_key, model="text-embedding-3-small")

# SemanticChunker 결과로 생성한 index로 검색했을 때, 
# "비영리민간단체" 단어는 1회 나오는데 이 단어가 포함된 제57조의2 내용이 모두 나옴, 의미론적으로 청킹해서 조 단위로 청킹된 것으로 생각됨
# vector_index = FAISS.load_local("../models/faiss_medical_law.json",
#                                 embeddings=embed_model, allow_dangerous_deserialization=True) # SemanticChunker
vector_index = FAISS.load_local("../models/faiss_medical_law_rec.json",
                                embeddings=embed_model, allow_dangerous_deserialization=True) # RecursiveCharacterTextSplitter
retrieved = vector_index.similarity_search("비영리민간단체")
print(f"retrieved len : {len(retrieved)}")
print(f"content : {retrieved[0].page_content}")

