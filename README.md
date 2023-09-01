# Data Structures Lab - README

# Description
This Python lab aims to practice working with sequences, comprehensions, and built-in methods for data structures. Specifically, we will work with a list of dictionaries representing various spicy foods and create functions to manipulate this data.

# Functions

get_names()
Returns a list of names of the spicy foods.
get_spiciest_foods()
Returns a list of spicy foods with a heat level greater than 5.
print_spicy_foods()
Prints the spicy foods in a specified format.
get_spicy_food_by_cuisine()
Returns a single dictionary for a spicy food based on its cuisine.
print_spiciest_foods()
Prints only the spiciest foods in a specified format.
get_average_heat_level()
Returns the average heat level of all spicy foods.
create_spicy_food()
Adds a new spicy food to the list of spicy foods.

# Usage

Clone this repository.
Open the data_structures.py file in the lib/ folder.
Implement the functions described above.
Run pytest -x to test your code.

# Example
python
Copy code
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    # ... (other spicy food entries)
]

# Call the functions as needed to work with the spicy_foods data.
Author
Mr.Perfect 092 (Stephan Maina)

License
This project is licensed under the MIT License - see the LICENSE file for details.

When all of your tests are passing, submit your work using `git`.

***

## Resources

- [Python List/Array Methods - W3Schools](https://www.w3schools.com/python/python_ref_list.asp)
- [Python Dictionary Methods - W3Schools](https://www.w3schools.com/python/python_ref_dictionary.asp)
- [When to Use a List Comprehension in Python - Real Python](https://realpython.com/list-comprehension-python/)
