import os
import sys
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

client = genai.Client(api_key=api_key)

def generate_content_with_retry(messages, max_retries=3, delay=2, verbose=False):
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash-001',
                contents=messages
            )
            if verbose:
                print(f"Working on: {prompt}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            return response
        except ServerError as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {str(e)}")
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise Exception(f"Failed after {max_retries} attempts: {str(e)}")

try:
    args = sys.argv[1:]
    
    # Check for --verbose flag
    be_verbose = False
    if '--verbose' in args:
        be_verbose = True
        args.remove('--verbose')
    
    prompt = ' '.join(args)

    if not prompt:
        print("Prompt not provided!")
        exit(1)
    
    messages = [
        genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)]),
    ]

    response = generate_content_with_retry(messages, verbose=be_verbose)

    print(response.text)
except Exception as e:
    print(f"Error: {str(e)}")
