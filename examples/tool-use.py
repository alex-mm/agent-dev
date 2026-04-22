# L04 - Tool Use Design Pattern
# Source: https://github.com/microsoft/ai-agents-for-beginners/tree/main/04-tool-use

import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_AI_PROJECT_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-05-01-preview"
)

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o")

TIMEZONE_DATA = {
    "san francisco": "America/Los_Angeles",
    "new york": "America/New_York",
    "london": "Europe/London",
    "tokyo": "Asia/Tokyo",
    "beijing": "Asia/Shanghai",
}

# Function description for the model to read
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    }
]

# Initial user message
messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

# First API call: Ask the model to use the function
response = client.chat.completions.create(
    model=deployment_name,
    messages=messages,
    tools=tools,
    tool_choice="auto",
)

# Process the model's response
response_message = response.choices[0].message
messages.append(response_message)

print("Model's response:")
print(response_message)


def get_current_time(location):
    """Get the current time for a given location"""
    print(f"get_current_time called with location: {location}")
    location_lower = location.lower()

    for key, timezone in TIMEZONE_DATA.items():
        if key in location_lower:
            print(f"Timezone found for {key}")
            current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
            return json.dumps({
                "location": location,
                "current_time": current_time
            })

    print(f"No timezone data found for {location_lower}")
    return json.dumps({"location": location, "current_time": "unknown"})


# Handle function calls
if response_message.tool_calls:
    for tool_call in response_message.tool_calls:
        if tool_call.function.name == "get_current_time":
            function_args = json.loads(tool_call.function.arguments)
            time_response = get_current_time(
                location=function_args.get("location")
            )
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": "get_current_time",
                "content": time_response,
            })
else:
    print("No tool calls were made by the model.")

# Second API call: Get the final response from the model
final_response = client.chat.completions.create(
    model=deployment_name,
    messages=messages,
)

print(final_response.choices[0].message.content)
