import asyncio
from pydantic_ai import Agent

from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

class RephraseAgent():
    def __init__(self, agent: Agent,content: str):
        super().__init__()
        self.agent = agent
        self.content = content

    def run(self):
        content = self.agent.run_sync("properly format and rephrase the following content: \n" + self.content + "\nRespond only with the formatted content and nothing else.")
        return content.output
    
model = OpenAIModel(
    model_name='devstral', provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)

agent = Agent(model=model) 

summary = RephraseAgent(agent,"Some random content here. It is very long and has nothing else in it.")

print(summary.run())