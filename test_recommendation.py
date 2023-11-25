import unittest
from restaurant_recommendation import recommend_restaurants

class TestRestaurantRecommendation(unittest.TestCase):
    # Sample restaurant data (name, cuisine, rating)
    restaurants = [
        {"name": "Restaurant A", "cuisine": "Italian", "rating": 4.5},
        {"name": "Restaurant B", "cuisine": "Mexican", "rating": 4.0},
        {"name": "Restaurant C", "cuisine": "Japanese", "rating": 4.2},
        {"name": "Restaurant D", "cuisine": "Indian", "rating": 3.8},
        # Add more restaurant data here
    ]

    # Test case for valid user preferences
    def test_valid_user_preferences(self):
        user_input = ["Italian", "Japanese", "Done"]
        expected_output = [
            {"name": "Restaurant A", "cuisine": "Italian", "rating": 4.5},
            {"name": "Restaurant C", "cuisine": "Japanese", "rating": 4.2}
        ]
        self.assertEqual(recommend_restaurants(user_input, self.restaurants), expected_output)

    # Test case for user preferences with no recommendations
    def test_no_recommendations(self):
        user_input = ["Mexican", "Indian", "Done"]
        expected_output = []
        self.assertEqual(recommend_restaurants(user_input, self.restaurants), expected_output)

    # Test case for invalid user input
    def test_invalid_user_input(self):
        user_input = ["Chinese", "Italian", "Done"]
        expected_output = [
            {"name": "Restaurant A", "cuisine": "Italian", "rating": 4.5}
        ]
        self.assertEqual(recommend_restaurants(user_input, self.restaurants), expected_output)

    # Test case for empty user input
    def test_empty_user_input(self):
        user_input = ["Done"]
        expected_output = []
        self.assertEqual(recommend_restaurants(user_input, self.restaurants), expected_output)

if __name__ == '__main__':
    unittest.main()
