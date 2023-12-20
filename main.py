from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI

def main():
    
    load_dotenv(find_dotenv())
    llm = OpenAI(model_name="text-davinci-003")

    try:
        print(llm(input()))
    except KeyboardInterrupt:
        pass

    return 0

if __name__ == "__main__":
    main()