import os
from dotenv import load_dotenv
from openai import OpenAI
 
load_dotenv(override=True)
client = OpenAI(base_url=os.getenv("BASE_URL"),
                api_key=os.getenv("API_KEY"))
MODEL = os.getenv("MODEL")
PRICE_IN, PRICE_OUT, INR = 0.075, 0.30, 94.0   # $/1M tokens, ₹/$
 
history = [{"role": "system",
            "content": ("You are a concise retail-bank assistant. Only answer "
                        "banking questions; politely decline anything else.")}]
def ask(question):
    history.append({"role": "user", "content": question})
    resp = client.chat.completions.create(
        model=MODEL, messages=history)
    answer = resp.choices[0].message.content
    history.append({"role": "assistant", "content": answer})
    u = resp.usage
    cost = (u.prompt_tokens * PRICE_IN
            + u.completion_tokens * PRICE_OUT) / 1e6 * INR
    return answer, u, cost
def main():
    total = 0.0
    print(f"Bank assistant on {MODEL}. Type 'quit' to exit.")
    while True:
        question = input("\nYou: ").strip()
        if question.lower() in {"quit", "exit"}:
            break
        if not question:
            continue
        answer, u, cost = ask(question)
        total += cost
        print(f"Bot: {answer}")
        print(f"[in {u.prompt_tokens} · out {u.completion_tokens} · ₹{cost:.4f} this turn · ₹{total:.4f} total]")
if __name__ == "__main__":
    main()
    