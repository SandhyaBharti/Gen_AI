from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load environment variables
load_dotenv()

print("____________________Welcome, Type '0' to exit this app____________________")
print("1. Funny")
print("2. Angry")
print("3. Sarcastic")
print("4. Sad")
print("5. Romantic")

personalities = {
    "1": "You are a funny and witty AI assistant.",
    "2": "You are an angry AI assistant.",
    "3": "You are a sarcastic AI assistant.",
    "4": "You are a sad and unhappy AI assistant.",
    "5": "You are a romantic AI assistant."
}

choice = input("\nChoose personality (1-5): ")

if choice not in personalities:
    print("Invalid choice")
    exit()

# Initialize conversation
messages = [
    SystemMessage(content=personalities[choice])
]

# Create model once
model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.9,
    max_tokens=100
)

while True:
    prompt = input("YOU: ")

    if prompt == "0":
        print("Goodbye!")
        break

    messages.append(HumanMessage(content=prompt))

    try:
        res = model.invoke(messages)

        messages.append(
            AIMessage(content=res.content)
        )

        print("BOT:", res.content)

    except Exception as e:
        print("Error:", e)