import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <text for prompt>")
    sys.exit(1)

prompt = sys.argv[1]

messages = [
    types.Content(role='user', parts=[types.Part(text=prompt)]),
]


response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
)

def set_verbose(args):
    args = args[1:]
    verbose = False
    for arg in args:
        if arg == "--verbose":
           verbose = True
    return verbose

def generate_response(args):
    prompt = args[1]
    verbose = set_verbose(args[1:])

    if verbose == True:
        print(f"User prompt: {prompt}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response: {response.text}")
    else:
        print(response.text)
    
def main():
    generate_response(sys.argv)

if __name__ == "__main__":
    main()
