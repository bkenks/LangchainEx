from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

def main():
    
    load_dotenv(find_dotenv())
    llm = OpenAI()
    chat_model = ChatOpenAI()

    text = "What would be a good company name for a company that makes colorful socks?"
    messages = [HumanMessage(content=text)]

    # Uncomment to use LLM Text Model
    #llm.invoke(text)

    # Uncomment to use ChatModel
    #chat_model.invoke(messages)


if __name__ == "__main__":
    main()