import os
import sys
import constants

# For your own data
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

# For global data
from langchain.llms import OpenAI  # OpenAI LLMS is paid but is the best
from langchain.chat_models import ChatOpenAI

# for Directory Loading
# from langchain.document_loaders import DirectoryLoader

os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY

query = sys.argv[1]

loader = TextLoader("data.txt")
# loader = DirectoryLoader(".", glob=".txt")  # load all .txt files from current dir

index = VectorstoreIndexCreator().from_loaders([loader])

# hybrid ai:hem locak hem de openai'ya bakar
# print(
#     index.query(query, llm=ChatOpenAI())
# )

print(index.query(query))
