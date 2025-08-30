from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import ListSortOrder
from dotenv import load_dotenv
import os

load_dotenv(override=True)

agent_endpoint = os.environ["AZURE_AGENT_ENDPOINT"]
agent_id = os.environ["AZURE_AGENT_ID"]

project = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=agent_endpoint)

agent = project.agents.get_agent(agent_id)

thread = project.agents.threads.create()
print(f"Created thread, ID: {thread.id}")

# DH added code
def call_agent(question):
    message = project.agents.messages.create(
        thread_id=thread.id,
        role="user",
        content=question)

    run = project.agents.runs.create_and_process(
        thread_id=thread.id,
        agent_id=agent.id)

    if run.status == "failed":
        print(f"Run failed: {run.last_error}")
    else:
        messages = project.agents.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)

    for message in messages:
        if message.text_messages:
            print(f"{message.role}: {message.text_messages[-1].text.value}")
            
while True:
    user_input = input("Enter your question: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    call_agent(user_input)
            