from dotenv import load_dotenv

load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    max_tokens=500,
    temperature=0.2
)
model = ChatHuggingFace(
    llm = llm
)
response = model.invoke("Hello, how are you?")
print(response.content)