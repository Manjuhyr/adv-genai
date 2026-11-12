
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv(override=True)

# Initialize Groq client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

MODEL = os.getenv("MODEL")

PRICE_IN, PRICE_OUT, INR = 0.075, 0.30, 95.0

history = [
    {
        "role": "system",
        "content": "You are a concise retail-banking assistant."
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

    usage = response.usage

    cost = (
        usage.prompt_tokens * PRICE_IN
        + usage.completion_tokens * PRICE_OUT
    ) / 1_000_000 * INR

    return answer, usage, cost


# Main program
if __name__ == "__main__":

    print("Welcome to Retail Banking Assistant!")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ")

        if question.lower() == "exit":
            print("Thank you for using Banking Assistant!")
            break

        try:
            answer, usage, cost = ask(question)

            print("\nBanking Assistant:", answer)
            print("\nToken Usage:")
            print("Prompt tokens:", usage.prompt_tokens)
            print("Completion tokens:", usage.completion_tokens)
            print(f"Estimated cost: ₹{cost:.6f}")
            print("-" * 50)

        except Exception as e:
            print("Error:", e)
