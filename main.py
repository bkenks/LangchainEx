from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

def main():
    
    # Variables and .env
    load_dotenv(find_dotenv())
    llm = OpenAI(model_name="text-davinci-003")

    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}",
    )

    
    print(llm(prompt.format(product="Smart Apps using Large Language Models (LLMs)")))


if __name__ == "__main__":
    main()