# Source Video: https://youtu.be/lG7Uxts9SXs

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv

load_dotenv()


def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.5)  # temp is for creativity, 1 is best creativity

    prompt_template_name = PromptTemplate(
        input_variables=["animal_type"],
        template="I have a {animal_type} pet and I will give a cool name to it, it is {pet_color} in color. Suggest me five cool names for my pet",
    )

    name_chain = LLMChain(
        llm=llm, prompt=prompt_template_name, output_key="pet_name"
    )  # output_keyis for calling from streamlit. look yz_streamlit.py

    response = name_chain({"animal_type": animal_type, "pet_color": pet_color})

    return response


if __name__ == "__main__":
    print(generate_pet_name("cow", "white"))  # returns JSON response
