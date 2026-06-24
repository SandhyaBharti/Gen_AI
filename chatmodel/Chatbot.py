from dotenv import load_dotenv

load_dotenv()
from langchain_mistralai import ChatMistralAI

print("_____________________________Welcome, Type 'Exit' to quit_____________________________________________")
while True:
    prompt = input("YOU: ")
    if prompt.lower() == "exit":
        break
    model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)
    res = model.invoke(prompt)
    print("AI: ",res.content)