from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are an AI assistant named Trinity skilled in general " \
        "tasks like Alexa or Google Assistant."),
    contents="hello there"
)

print(response.text)



