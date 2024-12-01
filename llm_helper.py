from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(model='llama-3.1-70b-versatile')

if __name__=='__main__':
    response = llm.invoke('What is the skills required to get a generative ai job')
    print(response.content)
