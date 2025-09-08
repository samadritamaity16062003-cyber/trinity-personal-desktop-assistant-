# from openai import OpenAI
# client = OpenAI(
#     api_key="sk-ijklmnop1234qrstijklmnop1234qrstijklmnop"
# )

# # Using Chat Completions API
# completion = client.chat.completions.create(
#     model="gpt-5",
#     messages=[
#         {"role": "system", "content": "You are an AI assistant named Trinity skilled in general tasks like Alexa or Google Assistant."},
#         {"role": "user", "content": "What is coding?"}
#     ]
# )

# # Correct way to access the response
# print(completion.choices[0].message["content"])



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



