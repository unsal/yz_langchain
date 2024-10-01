# Source Video: https://youtu.be/lG7Uxts9SXs

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(temperature=0.5)  # temp is for creativity, 1 is best creativity

prompt = PromptTemplate(
    # input_variables=["animal_type","pet_color"],
    template="I have a {animal_type} pet and I will give a cool name to it, it is {pet_color} in color. Suggest me five cool names for my pet"
)

output_parser = StrOutputParser()

chain =  prompt | llm | output_parser

output = chain.invoke({"animal_type": "cow", "pet_color": "white"})

print(output)


