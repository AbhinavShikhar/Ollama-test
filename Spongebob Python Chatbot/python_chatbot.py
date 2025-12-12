from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model= "chatbob")
prompt = ChatPromptTemplate.from_template("""{user_input}""")
parser = StrOutputParser()

chain = prompt | model | parser

loop = True

while loop:
    user_input = input("What do you want to say to Spongebob? ")
    if user_input != "bye":
        response = chain.invoke({"user_input":user_input})
        print(response)

    if user_input == "bye":
        response = chain.invoke({"user_input":user_input})
        print(response)
        loop = False
