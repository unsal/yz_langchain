
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(
    model_name="gpt-3.5-turbo", # not neccessary
    temperature = 0.5
)

text = "What is the Capitol of China?"

response = chat_model.invoke(text)

print(response)
