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
    names = []
    for food in spicy_foods:
        names.append(food['name'])
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_food = []
    for food in spicy_foods:
        spice_level = food["heat_level"]
        if spice_level > 5:
           spiciest_food.append(food)
           return spicy_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        spiciness_level = food['spiciness_level']
        heat_level = '🌶' * spiciness_level
        print(f"{name} | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    cuisine_foods = dict()
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            cuisine_foods[food["name"]] = food
    return cuisine_foods

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food['name']
            spiciness_level = food['spiciness_level']
            heat_level = '🌶' * spiciness_level
            print(f"{name} | Heat Level: {heat_level}")  
    

def get_average_heat_level(spicy_foods):
    heat_level = 0
    for food in spicy_foods:
        heat_level += food["heat_level"]
        average = heat_level / len(food)
        return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_food = dict()
    spicy_food["name"] = spicy_food["name"]
    spicy_food["cuisine"] = spicy_food["cuisine"]
    spicy_food["heat_level"] = spicy_food["heat_level"]
    spicy_foods.append(spicy_food)
    return spicy_foods

