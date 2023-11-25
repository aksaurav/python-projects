import unittest
from restaurant_recommendation import get_user_preferences

class TestUserPreferences(unittest.TestCase):
    # Test case for valid user preferences and location
    def test_valid_user_preferences_location(self):
        available_cuisines = ["Italian", "Japanese", "Mexican", "Indian"]
        user_input = (["Italian", "Japanese", "Done"], (40.7306, -73.9352))
        expected_output = (["Italian", "Japanese"], (40.7306, -73.9352))
        self.assertEqual(get_user_preferences(*user_input, available_cuisines), expected_output)

    # Test case for invalid user input for cuisine preference
    def test_invalid_user_input_cuisine(self):
        available_cuisines = ["Italian", "Japanese", "Mexican", "Indian"]
        user_input = (["Chinese", "Done"], ())
        expected_output = ([], ())
        self.assertEqual(get_user_preferences(*user_input, available_cuisines), expected_output)

    # Test case for empty user input for location
    def test_empty_user_input_location(self):
        available_cuisines = ["Italian", "Japanese", "Mexican", "Indian"]
        user_input = (["Done"], ())
        expected_output = ([], ())
        self.assertEqual(get_user_preferences(*user_input, available_cuisines), expected_output)

if __name__ == '__main__':
    unittest.main()
