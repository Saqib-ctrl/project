import os
import requests
from dotenv import load_dotenv
from backend import schemas

load_dotenv()

def generate_openrouter_response(prompt: str):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
        response.raise_for_status()
        resp_json = response.json()
        print("DEBUG OpenRouter raw response:", resp_json)
        if "choices" in resp_json:
            return resp_json["choices"][0]["message"]["content"].strip()
        elif "error" in resp_json:
            return f"OpenRouter Error: {resp_json['error'].get('message', 'Unknown')}"
        else:
            return "OpenRouter returned an unexpected format"
    except Exception as e:
        return f"Request failed: {str(e)}"

def generate_blog(data: schemas.BlogInput):
    prompt = (
        f"Write a professional blog post titled '{data.title}' for an audience of {data.audience}. "
        f"The purpose is: {data.purpose}. The tone should be informative and engaging."
    )
    return {"content": generate_openrouter_response(prompt)}
