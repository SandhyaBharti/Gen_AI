#MovieSage AI bot
#1. take a raw para about a movie
#2. Extract important structure info
#3. Generate a clean summary
#4. Returns it into JSON format


from dotenv import load_dotenv
load_dotenv()

# prompts templates
from langchain_core.prompts import ChatPromptTemplate

from langchain_mistralai import ChatMistralAI

model=ChatMistralAI(model="mistral-small-2603")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are MovieSage AI, an expert movie analyst.

Your tasks:
1. Read the movie description
2. Extract structured data
3. Summarize the movie
4. Return ONLY valid JSON

Output format:
{{
  "title": "",
  "genre": "",
  "cast": [],
  "plot_summary": "",
  "final_summary": ""
}}

Rules:
- Output must be ONLY JSON
- No extra text
"""
    ),
    ("human", "{movie_description}")
])

para = input("give your paragraph")
final_prompt = prompt.invoke({"movie_description": para})
res = model.invoke(final_prompt)
print(res.content)

