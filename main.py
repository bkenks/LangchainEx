from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate

def main():
    
    # Variables and .env
    load_dotenv(find_dotenv())
    llm = OpenAI(model_name="text-davinci-003")

    try:
        print(llm(input()))
    except KeyboardInterrupt:
        pass



if __name__ == "__main__":
    main()