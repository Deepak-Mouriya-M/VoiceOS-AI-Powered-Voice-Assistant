import requests
from config import OLLAMA_URL, MODEL_NAME


def ask_ai(message):
    url = f"{OLLAMA_URL}/api/chat"

    data = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are Jarvis, a helpful personal AI assistant. "
                    "Give clear and concise answers."
                )
            },
            {
                "role": "user",
                "content": message
            }
        ],
        "stream": False
    }

    try:
        response = requests.post(url, json=data, timeout=120)
        response.raise_for_status()

        result = response.json()
        return result["message"]["content"]

    except requests.exceptions.RequestException as e:
        return f"Ollama connection error: {e}"

    except Exception as e:
        return f"AI error: {e}"