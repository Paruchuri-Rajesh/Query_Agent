from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

web_agent=Agent(
    name="WebAgent"
    ,model=OpenAIChat(model="gpt-4-0613")
    ,tools=[DuckDuckGo()]   ,
    instructions="You are a helpful web agent that can search the web using DuckDuckGo to find information for users."
    ,markdown=True,
    show_tool_calls=True,
)

web_agent.print_response("What is the capital of France?",stream=True)
