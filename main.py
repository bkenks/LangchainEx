from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI
from langchain import ConversationChain

def main():
    
    load_dotenv(find_dotenv())
    llm = OpenAI(model_name="text-davinci-003")

    conversation = ConversationChain(llm=llm, verbose=1)

    output = conversation.predict(input="Hi there!")
    print(output)

    output = conversation.predict(input="I'm doing well. What was the first thing I said to you just before this?")
    print(output)


if __name__ == "__main__":
    main()