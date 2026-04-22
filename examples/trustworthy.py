# L06 - Building Trustworthy AI Agents
# Source: https://github.com/microsoft/ai-agents-for-beginners/tree/main/06-building-trustworthy-agents

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Human-in-the-Loop: create a response and ask for user approval before finalizing
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# The user can review and approve the response
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
