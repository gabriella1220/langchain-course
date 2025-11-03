from dotenv import load_dotenv
from langchain_classic import hub #some communiity that allow us to download prompt shared by others
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
import os 
load_dotenv(override=True)

tools = [TavilySearch()]

llm = ChatOpenAI(model="gpt-4")
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(
    llm=llm,
    tools = tools, 
    prompt=react_prompt
)
agent_executor = AgentExecutor(agent=agent,tools=tools, verbose=True)
chain = agent_executor

def main():
    result = chain.invoke(
        input ={
            "input":"search for 3 job postings for an ai engineer using langchain in the stamford ct atea on linkedin and list their details and post most recently"
            ""
        }
    )
    print(result)

if __name__ == "__main__":

    main()
