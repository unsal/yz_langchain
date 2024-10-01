
from langchain_openai import ChatOpenAI, OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()
chat_model = ChatOpenAI()

text = "Tell me a joke about Einstein"

# llm returns TEXT
print("LLM MODEL:")
llm_response = llm.invoke(text)
print(llm_response)

# chat model returns MESSAGE OBJECT
print("")
print("CHAT MODEL:")
chat_model_response = chat_model.invoke(text)
print(chat_model_response)