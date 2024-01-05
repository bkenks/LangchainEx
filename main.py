from dotenv import load_dotenv, find_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

def main():
    
    load_dotenv(find_dotenv())

    # Takes user-given context, embeds it, then stores it in a vector store
    vectorStore = FAISS.from_texts(
        ["harrison worked at kensho", "bears like to eat apples"],
        embedding=OpenAIEmbeddings()
        )
    
    # not really sure what this does
    retreiver = vectorStore.as_retriever()

    template = """Answer the question based only on the following context:
    {context}
    
    Question: {question}
    """

    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI()
    outputParser = StrOutputParser()

    setupAndRetreival = RunnableParallel(
        {"context": retreiver, "question": RunnablePassthrough()}
    )

    chain = setupAndRetreival | prompt | llm | outputParser

    print(chain.invoke("Where did harrison work?"))


if __name__ == "__main__":
    main()