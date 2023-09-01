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
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food['name'] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_food = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_food

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        heat_level = '🌶' * food['heat_level']
        print(f"{name} | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    cuisine_foods = {food["name"]: food for food in spicy_foods if food["cuisine"] == cuisine}
    return cuisine_foods

def get_average_heat_level(spicy_foods):
    heat_level_sum = sum(food["heat_level"] for food in spicy_foods)
    average = heat_level_sum / len(spicy_foods)
    return average

def create_spicy_food(spicy_foods, new_food):
    spicy_foods.append(new_food)
    return spicy_foods

# Test the functions
if __name__ == "__main__":
    print("Names of Spicy Foods:")
    names = get_names(spicy_foods)
    print(names)

    print("\nSpiciest Foods:")
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

    print("\nSpicy Foods by Cuisine (Thai):")
    thai_foods = get_spicy_food_by_cuisine(spicy_foods, "Thai")
    print_spicy_foods(thai_foods.values())

    print("\nAverage Heat Level:", get_average_heat_level(spicy_foods))

    new_food = {
        "name": "Spicy Ramen",
        "cuisine": "Japanese",
        "heat_level": 7,
    }
    spicy_foods = create_spicy_food(spicy_foods, new_food)
    print("\nUpdated Spicy Foods:")
    print_spicy_foods(spicy_foods)

