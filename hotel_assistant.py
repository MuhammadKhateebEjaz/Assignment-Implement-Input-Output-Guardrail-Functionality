
# hotel_assistant.py
# Dynamic hotel booking assistant with multiple hotels
# Based on bilal_fareed_code example

from openai import OpenAI
from openai.agents import Agent, Tool

client = OpenAI()

# ---------------------------
# Hotel Database (Dynamic)
# ---------------------------
hotels = {
    "hotel paradise": {
        "location": "Karachi",
        "price": "PKR 10,000 per night",
        "rooms": "Deluxe, Suite, Standard"
    },
    "ocean view": {
        "location": "Gwadar",
        "price": "PKR 15,000 per night",
        "rooms": "Sea View Suite, Family Room"
    },
    "mountain lodge": {
        "location": "Murree",
        "price": "PKR 8,000 per night",
        "rooms": "Cabins, Standard, Luxury Suite"
    }
}

# ---------------------------
# Tool: Retrieve Hotel Info
# ---------------------------
def get_hotel_info(query: str):
    query_lower = query.lower()
    for name, details in hotels.items():
        if name in query_lower:
            return f"🏨 {name.title()} - Location: {details['location']}, Price: {details['price']}, Rooms: {details['rooms']}"
    return "❌ Sorry, I don’t have information about that hotel."

hotel_info_tool = Tool(
    name="hotel_information_tool",
    description="Provides details about hotels based on user queries",
    fn=get_hotel_info
)

# ---------------------------
# Agent Setup
# ---------------------------
agent = Agent(
    client=client,
    model="gpt-4.1-mini",
    tools=[hotel_info_tool],
    instructions="You are a hotel booking assistant. Help users by providing details of the hotel they ask about."
)

# ---------------------------
# Run Example
# ---------------------------
if __name__ == "__main__":
    print(agent.run("Tell me about Hotel Paradise"))
    print(agent.run("Do you have info on Ocean View?"))
    print(agent.run("I want to book Mountain Lodge"))
    print(agent.run("What about Royal Palace Hotel?"))
