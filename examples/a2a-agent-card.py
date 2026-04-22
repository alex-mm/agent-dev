# L11 - Agentic Protocols: A2A Agent Card
# Source: https://github.com/microsoft/ai-agents-for-beginners/tree/main/11-agentic-protocols

# A2A Agent Card registration example
agent_card = {
    "name": "FlightBookingAgent",
    "description": "专业航班预订 Agent",
    "skills": [
        {"name": "search_flights", "description": "搜索可用航班"},
        {"name": "book_flight", "description": "预订航班"},
    ],
    "endpoint": "https://your-a2a-agent-host/agents/flight",
    "version": "1.0",
}

# A2A remote agent via Microsoft Agent Framework
# from agent_framework.azure import AzureAIProjectAgentProvider
# from azure.identity import AzureCliCredential
#
# agent = A2AAgent(
#     name=agent_card["name"],
#     description=agent_card["description"],
#     agent_card=agent_card,
#     url="https://your-a2a-agent-host"
# )
