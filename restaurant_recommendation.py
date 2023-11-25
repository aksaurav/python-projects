import math

# Sample restaurant data (name, cuisine, rating, proximity)
restaurants = [
        {"name": "Restaurant A", "cuisine": "Italian", "rating": 4.5, "location": (40.7128, -74.0060)},
        {"name": "Restaurant B", "cuisine": "Mexican", "rating": 4.0, "location": (34.0522, -118.2437)},
        {"name": "Restaurant C", "cuisine": "Japanese", "rating": 4.2, "location": (41.8781, -87.6298)},
    ]


# Function to calculate distance between two geographic coordinates using Haversine formula
def calculate_distance(loc1, loc2):
    R = 6371  # Radius of the Earth in kilometers

    lat1, lon1 = loc1
    lat2, lon2 = loc2

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c  # Distance in kilometers
    return distance

# Function to recommend restaurants based on user preferences, ratings, and proximity
def recommend_restaurants(preferences, restaurants_list, user_location, max_distance=10, min_rating=4.0):
    recommended_restaurants = []

    for restaurant in restaurants_list:
        # Check if the restaurant cuisine matches user preferences
        if restaurant["cuisine"] in preferences:
            # Calculate distance between user and the restaurant
            distance = calculate_distance(user_location, restaurant["location"])

            # Check if the distance is within the specified maximum distance
            # and if the restaurant rating is above the minimum rating
            if distance <= max_distance and restaurant["rating"] >= min_rating:
                recommended_restaurants.append(restaurant)

    return recommended_restaurants


# Get available cuisines from the restaurant data
available_cuisines = set(restaurant["cuisine"] for restaurant in restaurants)

# Get user preferences for cuisines and location
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
    
    # Get user's location coordinates
    user_location = ()
    while True:
        try:
            lat = float(input("Enter your latitude: "))
            lon = float(input("Enter your longitude: "))
            user_location = (lat, lon)
            break
        except ValueError:
            print("Please enter valid numeric values for latitude and longitude.")

    return preferences, user_location


# Get user preferences for cuisines and location
user_preferences, user_location = get_user_preferences()

# Get recommendations based on user preferences, location, and minimum rating
recommendations = recommend_restaurants(user_preferences, restaurants, user_location)


# Print recommended restaurants
if recommendations:
    print("Recommended Restaurants:")
    for restaurant in recommendations:
        print(f"{restaurant['name']} ({restaurant['cuisine']}) - Rating: {restaurant['rating']}")
else:
    print("No recommendations found for your preferences.")
