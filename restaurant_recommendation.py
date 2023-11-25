# Sample restaurant data (name, cuisine, rating)
restaurants = [
    {"name": "Restaurant A", "cuisine": "Italian", "rating": 4.5},
    {"name": "Restaurant B", "cuisine": "Mexican", "rating": 4.0},
    {"name": "Restaurant C", "cuisine": "Japanese", "rating": 4.2},
    {"name": "Restaurant D", "cuisine": "Indian", "rating": 3.8},
    # Add more restaurant data here
]

# Function to recommend restaurants based on user preferences and ratings
def recommend_restaurants(preferences, restaurants_list, min_rating=4.0):
    recommended_restaurants = []

    for restaurant in restaurants_list:
        # Check if the restaurant cuisine matches user preferences
        if restaurant["cuisine"] in preferences and restaurant["rating"] >= min_rating:
            recommended_restaurants.append(restaurant)

    return recommended_restaurants

# Get available cuisines from the restaurant data
available_cuisines = set(restaurant["cuisine"] for restaurant in restaurants)

# Get user preferences for cuisines
def get_user_preferences():
    preferences = []
    while True:
        preference = input("Enter your preferred cuisine (or 'done' to finish): ").strip().capitalize()
        if preference == 'Done':
            break
        if preference not in available_cuisines:
            print('Sorry, that cuisine is not available. Please choose from:', available_cuisines)
            continue
        preferences.append(preference)
    return preferences

# Get user preferences for cuisines
user_preferences = get_user_preferences()

# Get recommendations based on user preferences and minimum rating
recommendations = recommend_restaurants(user_preferences, restaurants)

# Print recommended restaurants
if recommendations:
    print("Recommended Restaurants:")
    for restaurant in recommendations:
        print(f"{restaurant['name']} ({restaurant['cuisine']}) - Rating: {restaurant['rating']}")
else:
    print("No recommendations found for your preferences.")
