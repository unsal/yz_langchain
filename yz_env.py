# Source Video: https://youtu.be/lG7Uxts9SXs

from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()


def generate_pet_name():
    llm = OpenAI(temperature=0.5)  # temp is for creativity, 1 is best creativity

    name = llm(
        "I have a dog pet and I will give a cool name to it. Suggest me five cool names for my pet"
    )

    return name


if __name__ == "__main__":
    print(generate_pet_name())
