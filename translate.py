from dotenv import load_dotenv

load_dotenv

from openai import OpenAI
client = OpenAI()

english_text = "How are you?"

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role":"system","content":"You are helpful assistant"},
         {"role":"user","content": f'''Translate the following text to french: "{english_text}" '''},
    ],
)

print(response)