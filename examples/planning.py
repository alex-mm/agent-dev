# L07 - Planning Design Pattern
# Source: https://github.com/microsoft/ai-agents-for-beginners/tree/main/07-planning-design

import json
import os
from enum import Enum
from typing import List
from pprint import pprint

from pydantic import BaseModel
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"


# Travel SubTask Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # we want to assign the task to the agent


class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool


provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = provider.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))

# Iterative re-planning with previous context
system_prompt_replan = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

previous_plan = TravelPlan(
    main_task="Plan a family trip from Singapore to Melbourne.",
    subtasks=[
        TravelSubTask(
            task_details="Book round-trip flights from Singapore to Melbourne.",
            assigned_agent=AgentEnum.FlightBooking,
        )
    ],
    is_greeting=False,
)

response_replan = provider.create_response(
    input=user_message,
    instructions=system_prompt_replan,
    context=f"Previous travel plan - {previous_plan}",
)
