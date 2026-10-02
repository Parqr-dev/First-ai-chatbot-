import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"
model = "openai/gpt-oss-120b"
while True:
    data = input(" Ask a question or enter None to quit: ").title()
    if data == "None":
        break
    header = {
        "Authorization" : f"Bearer {api_key}",
        "Content-Type" : "application/json"
    }
    data = {
        "model" : model,
        "messages" : [
            {
            "role" : "user",
            "content" : data
            }
        ]
    }
    try:
        reponse = requests.post(url,headers=header,json = data)
        answer  = reponse.json()
        print("Agent :"," ",answer["choices"][0]["message"]["content"])
    except Exception as e:
        print(e)