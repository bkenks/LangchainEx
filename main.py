from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents.load_tools import get_all_tool_names

def main():
    
    load_dotenv(find_dotenv())
    davinciLLM = OpenAI(model_name="text-davinci-003")

    tools = load_tools(["wikipedia", "llm-math"], llm=davinciLLM)
    wikiAgent = initialize_agent(
        tools, davinciLLM, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=1
    )
    
    print(wikiAgent.run(
        "In what year was python released and who is the original creator? Multiply the year by 3"
    ))


if __name__ == "__main__":
    main()