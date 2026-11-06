import os
from dotenv import load_dotenv

load_dotenv()

def call_llm_with_fallback(prompt: str):
    # Mock response for testing and development purposes
    primary_model = "mock-gpt-4o-mini"
    answer = f"Hello! This is a simulated support response regarding: '{prompt}'. Our team will look into your request."
    tokens = 42
    cost = 0.0001
    return answer, primary_model, tokens, cost