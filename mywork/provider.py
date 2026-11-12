
# providers.py
# YOU = type it by hand

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

GROQ = "https://api.groq.com/openai/v1"

PROVIDERS = {
    # YOU: name -> (url, key variable, model)

    "groq-small": (GROQ, "API_KEY", "openai/gpt-oss-20b"),

    "groq-large": (GROQ, "API_KEY", "openai/gpt-oss-120b"),

    "gemini": (
        "https://generativelanguage.googleapis.com/v1beta/openai/",
        "GEMINI_API_KEY",
        os.getenv("GEMINI_MODEL")
    ),

    "openrouter": (
        "https://openrouter.ai/api/v1",
        "OPENROUTER_API_KEY",
        "openrouter/free"
    ),

    "local": (
        "http://localhost:11434/v1",
        None,
        os.getenv("LOCAL_MODEL", "llama3.2:3b")
    ),
}


def connect(name):
    # YOU
    url, key_var, model = PROVIDERS[name]

    key = os.getenv(key_var) if key_var else "ollama"

    return OpenAI(base_url=url, api_key=key), model
