
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo", # not neccessary
    temperature = 0.5
)

text = "What is the Capitol of China?"

response = llm.invoke(text)

print(response)
