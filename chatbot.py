"""curl -X POST "https://api.groq.com/openai/v1/chat/completions" \
     -H "Authorization: Bearer $GROQ_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"messages": [{"role": "user", "content": "Explain the importance of fast language models"}], "model": "llama-3.3-70b-versatile"}'"""
import requests
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv("API_KEY")
apikey = "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"
headers = {
    "Authorization":f"Bearer {apikey}",
    "Accept":"application/json"

}
def get_answer(question):
    headers = {
         "Authorization":"user",
    "Accept":"question"
    }
data = {
    "messages":[
        {
            "role":"user",
            "content":"explain the importance of flask language model"
        }
    ],
    "model":"llama-3.3-70b-versatile"
}
res = requests.post("https://api.groq.com/openai/v1/chat/completions"
,headers=headers
,json=data)

print("status_code",res.status_code)

print("Data:",res.json())
answer = res.json()['choices'][0]['message']['content']
print(answer)
print(get_answer("Explain AI"))
print(get_answer("Explain Flask"))

