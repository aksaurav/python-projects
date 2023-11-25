# Restaurant Recommendation System

## Overview

This project implements a basic restaurant recommendation system based on user preferences and restaurant ratings. It allows users to input their preferred cuisines and generates restaurant recommendations that match those preferences and meet a minimum rating threshold.

## Code Description

### `recommend_restaurants` Function

- This function takes user preferences and a list of restaurants as input.
- It filters restaurants based on user preferences and a minimum rating.
- Returns a list of recommended restaurants that match the criteria.

### `get_user_preferences` Function

- Prompts the user to input their preferred cuisines.
- Validates the user inputs against available cuisines from the restaurant data.
- Returns a list of user preferences.

### Sample Restaurant Data

- Contains a list of dictionaries representing restaurant information (name, cuisine, rating).

## Usage

1. Run the code to prompt the user to input their preferred cuisines.
2. Enter cuisines one by one (type 'done' to finish).
3. The program will provide a list of recommended restaurants based on user preferences and minimum rating.

## How to Run

1. Ensure Python is installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the Python file.
4. Run the Python script using `python filename.py` (replace `filename.py` with the actual filename).

## Test Cases

- Test cases have been implemented using `unittest` to validate different scenarios.
- Tests cover scenarios such as valid user preferences, no recommendations, invalid user input, and empty user input.

## Conclusion

This project provides a basic example of a restaurant recommendation system in Python. It can be expanded and enhanced with additional features such as user ratings, location-based recommendations, or integration with external APIs.

## Additional Notes

- Consideration for scalability and optimization can be made for larger restaurant datasets.
- Enhancements could include implementing a graphical user interface (GUI) for better user interaction.
