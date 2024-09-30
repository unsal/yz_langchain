
# Hugging Face is the open source alternative for OpenAI. It's API KEY is free
# 1. Create Account on https://huggingface.co
# 2. hf > settings > access tokens > create token (give a name select write role)
# 3. copy token > put that token in to .env
#    HUGGINGFACEHUB_API_TOKEN = xxxxx
# 4. hf > select model > there is hunderds of modeks on hf.co.. select "google/flan-t5-large" for text translation
# 5. Copy repo_id for thet model assign it to repo_id arg
# 6. terminal > pip3 install huggingface_hub
# 7. run your code


from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

from langchain_community.llms import HuggingFaceHub

import os

hf = HuggingFaceHub(
    repo_id="google/flan-t5-large",
    model_kwargs={"temperature":0.7,"max_length":100},
    huggingfacehub_api_token = os.environ["HUGGINGFACEHUB_API_TOKEN"]
    )


text="What is the capitol of Holland?"
response = hf.invoke(text)
print(response)
