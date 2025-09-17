from typing import TypedDict, List
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

class AgentState(TypedDict):
    messages:List[HumanMessage]
    
def process(state:AgentState) -> AgentState:
    response = llm.invoke(state['messages'])
    print(f"\nAI: {response.content}")
    print(f"\nState: {state}")
    return state

graph = StateGraph(AgentState)

graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

agent  = graph.compile()

user_input = input("Enter: ")

while user_input != "exit":
    agent.invoke({"messages":[HumanMessage(content=user_input)]})
    user_input = input("Enter: ")