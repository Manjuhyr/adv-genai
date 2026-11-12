
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

MODEL = os.getenv("MODEL")

PRICE_IN, PRICE_OUT, INR = 0.075, 0.30, 95.0

history = [
    {
        "role": "system",
        "content": "You are concise retail-banking assistant."
    }
]


def ask(question):
    history.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model=MODEL,
        messages=history
    )

    answer = response.choices[0].message.content
    history.append({"role": "assistant", "content": answer})

    u = response.usage

    cost = (
        u.prompt_tokens * PRICE_IN
        + u.completion_tokens * PRICE_OUT
    ) / 1_000_000 * INR

    return answer, u, cost
print("Testing banking assistant...")
answer, usage, cost = ask("What is the capital of France?")

print("\nAnswer:", answer)
print("Usage:", usage)
print(f"Estimated cost: ₹{cost:.6f}")