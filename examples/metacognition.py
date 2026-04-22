# L09 - Metacognition in AI Agents: Travel_Agent with self-reflection
# Source: https://github.com/microsoft/ai-agents-for-beginners/tree/main/09-metacognition


def search_flights(preferences):
    return [{"flight": "CA1234", "price": 580}, {"flight": "MU5678", "price": 420}]


def search_hotels(preferences):
    return [{"hotel": "Grand Hotel", "price": 800}]


def search_attractions(preferences):
    return [{"attraction": "Louvre Museum"}, {"attraction": "Eiffel Tower"}]


def create_itinerary(flights, hotels, attractions):
    return {
        "flights": flights,
        "hotels": hotels,
        "attractions": attractions,
    }


def adjust_preferences(preferences, feedback):
    updated = preferences.copy()
    if "disliked" in feedback:
        updated["avoid"] = feedback["disliked"]
    return updated


class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)


# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
