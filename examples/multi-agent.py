# L02 - Explore Agentic Frameworks: Multi-Agent with Microsoft Agent Framework
# Source: https://github.com/microsoft/ai-agents-for-beginners/tree/main/02-explore-agentic-frameworks

import asyncio
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


async def retrieve_tool(query: str) -> str:
    """Retrieve relevant data using available tools."""
    return f"Retrieved data for: {query}"


async def analyze_tool(data: str) -> str:
    """Analyze the retrieved data and provide insights."""
    return f"Analysis complete for: {data}"


async def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

    # Single agent with tool calling
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)

    # Multiple agents working together
    agent_retrieve = await provider.create_agent(
        name="dataretrieval",
        instructions="Retrieve relevant data using available tools.",
        tools=[retrieve_tool],
    )

    agent_analyze = await provider.create_agent(
        name="dataanalysis",
        instructions="Analyze the retrieved data and provide insights.",
        tools=[analyze_tool],
    )

    # Run agents in sequence on a task
    retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
    analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
    print(analysis_result)


if __name__ == "__main__":
    asyncio.run(main())
