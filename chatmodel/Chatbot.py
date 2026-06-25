from langchain_core.messages import content
from dotenv import load_dotenv

load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage

messages = [
    SystemMessage(content = "You are a funny and witty AI "),
]
print("____________________Welcome, Type '0' to exit this app____________________")
print("1, Funny")
print("2, Angry")
print("3, Sarcastic")
print("4, Sad")
print("5, Romantic")

personalities = {
    "1": " U r a funny and witty AI assistant, if asked about any topic ",
    "2": "U r an angry AI agent",
    "3": "U r a Sarcastic AI agent",
    "4": "U r a sad and unhappy AI agent",
    "5": "U r a Romantic AI agent"
}
choice = input("\n Choose personality(1-5):")
if choice not in personalities:
    print("Invalid")
    exit()
while True:
    prompt = input("YOU: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)
    res = model.invoke(prompt)
    messages.append(AIMessage(content = res.content))
    print("BOT: ",res.content)
    # print(messages)
