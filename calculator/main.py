import os
import sys
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

client = genai.Client(api_key=api_key)

# Function declarations
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

# Available functions
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

def generate_content_with_retry(messages, max_retries=3, delay=2, verbose=False):
    for attempt in range(max_retries):
        try:
            system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
            response = client.models.generate_content(
                model='gemini-2.0-flash-001',
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt
                )
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

    # Check for function calls
    if response.candidates and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if hasattr(part, 'function_call'):
                print(f"Calling function: {part.function_call.name}({part.function_call.args})")
            else:
                print(part.text)
    else:
        print(response.text)

except Exception as e:
    print(f"Error: {str(e)}")
