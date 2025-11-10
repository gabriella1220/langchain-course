from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch 


from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse

load_dotenv(override=True)

tools = [TavilySearch()]

model = ChatOpenAI(model ='gpt-4')

agent = create_agent(
    model= model,
    tools = tools,
    response_format=AgentResponse
)



def main():
    result = agent.invoke(
       "messages":[
           {
               "role":"user",
               "content":"search for 3 job positings for ai enginere in stamford"

           }]
    )
    structured = result.get("structured_response",None)
    print(structured if structured is not None else result)

if __name__ == "__main__":
    main()

