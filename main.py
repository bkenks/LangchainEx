from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def main():
    
    load_dotenv(find_dotenv())
    llm = OpenAI(model_name="text-davinci-003")

    promptTemp = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )

    myChain = LLMChain(llm=llm, prompt=promptTemp)
    print(myChain.run("AI Chatbots for a Law Office"))


if __name__ == "__main__":
    main()