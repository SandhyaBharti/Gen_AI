from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

texts=[
    "Hello I am Sandhya Bharti",
    "Hii I am learning Gen AI",
    "Teacher is great and cute"
]
vector = embeddings.embed_documents(texts)
# print(vector)
# print(len(vector))
print(len(vector[0]))




