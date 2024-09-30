# Source Video: https://youtu.be/lG7Uxts9SXs

# Agent uses the tools in his environmet for better relevant data
# This sample uses Wikipedia
# To do this install Wikipedia by:
# pip3 install wikipedia
# pip3 install numexpr  (for math calculation in the question)

# from langchain.llms import OpenAI
from langchain_openai import OpenAI

# agent libs
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from dotenv import load_dotenv

load_dotenv()


def langchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(
        ["wikipedia", "llm-math"], llm=llm
    )  # to get this work: pip install wikipedia

    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    result = agent.run("What is the average age of a Dog? Multiple the age by 3")

    print(result)


if __name__ == "__main__":
    langchain_agent()
