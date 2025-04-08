# simple_example.py
from langchain.llms import OpenAI

# Initialize the OpenAI LLM.
# NOTE: This example assumes you have an OpenAI API key set as an environment variable
# named OPENAI_API_KEY. If not, set it up or replace the api_key parameter below.
llm = OpenAI(temperature=0.7)

# Ask the model a simple question
response = llm("Hello, how are you?")
print("Response:", response)
