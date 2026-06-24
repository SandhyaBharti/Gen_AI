from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI


# ---------------- GEMINI ----------------
gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
res1 = gemini.invoke("Hi Gemini, how are you?")
print("Gemini:", res1.content)


# ---------------- GROQ ----------------
groq = ChatGroq(model_name="openai/gpt-oss-120b")
res2 = groq.invoke("Hi Groq, how are you?")
print("Groq:", res2.content)


# ---------------- MISTRAL ----------------
mistral = ChatMistralAI(model="mistral-small-2603", temperature=0.2)
res3 = mistral.invoke("Tell me a short joke about coding.")
print("Mistral:", res3.content)


