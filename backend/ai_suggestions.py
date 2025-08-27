from ollama import chat
from ollama import ChatResponse

def ask_llama(prompt: str) -> str:
    response: ChatResponse = chat(model="llama3", messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ])
    return response["message"]["content"]

print(ask_llama("What is the capital of France?"))