#Imports
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
import os

class Agent:
    def __init__(self,config_value:str):
        self.__API_OPENROUTER = ""
        self.__API_TAVILY = os.environ["TAVILY_API_KEY"] = ""
        self.__model = "qwen/qwen3-coder:free"
        self.__baseURL = "https://openrouter.ai/api/v1"
        self.__model = ChatOpenAI(
            model_name = self.__model,
            base_url = self.__baseURL,
            api_key = self.__API_OPENROUTER
        )
        self.__config = {"configurable":{"thread_id": config_value}}
        self.memory = MemorySaver()
        self.tools = [TavilySearch(max_results=2)]
        
    def run(self):
        agent_executor = create_react_agent(self.__model, self.tools, checkpointer= self.memory)
        while True:
            prompt = input("\nIngresa un prompt: ")
            if not prompt or prompt.strip() == "":
                raise ValueError("El texto para la consulta no puede estar vacío")
            if prompt == "Adios":
                break
            input_message = {"role":"user","content":prompt}
            for step in agent_executor.stream(
                {"messages":[input_message]},
                self.__config,
                stream_mode="values"
            ):
                step["messages"][-1].pretty_print()
            
            prompt=""
            

if __name__ == "__main__":
    agent = Agent("prueba")
    agent.run()