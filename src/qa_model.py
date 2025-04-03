
import requests
import os

# Set your Perplexity API key
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")  # Or set it manually


def answer_question(question, context):
    try:
        url = "https://api.perplexity.ai/chat/completions"

        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "sonar",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a legal and financial expert analyzing term sheets so answer based on context."
                },
                {
                    "role": "user",
                    "content": f"Context: {context}\nQuestion: {question}\n."
                }
                
            ],
            "max_tokens": 500,
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        else:
            return f"Error: {response.status_code}, {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"