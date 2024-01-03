from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    
    load_dotenv(find_dotenv())
    prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
    model = ChatOpenAI()
    output_parser = StrOutputParser()

    chain = prompt | model | output_parser

    print(chain.invoke({"topic": "ice cream"}))


if __name__ == "__main__":
    main()