import time
import random

class Brew:
    INGREDIENT_SCORES = {
    "tea": {
        "jasmine": 3,
        "mint": 4,
        "lemon": 5,
        "sugar": 2,
        "honey": 4,
        "water": 1,
        "cardamom": 7,
        "ginger": 6,
        "cinnamon": 6,
        "rose_petals": 5,
        "black_tea": 3,
        "green_tea": 4,
        "oolong": 5,
        "chamomile": 4,
        "orange_peel": 5,
        "lavender": 6,
        "lime": 5,
        "strawberry": 6,
        "blueberry": 6,
        "pineapple": 7,
        "peach": 6
    },
    "coffee": {
        "espresso": 5,
        "milk": 3,
        "caramel": 4,
        "chocolate": 4,
        "sugar": 2,
        "water": 1,
        "vanilla": 7,
        "cinnamon": 6,
        "nutmeg": 5,
        "whipped_cream": 4,
        "hazelnut": 5,
        "almond_milk": 3,
        "coconut_milk": 4,
        "soy_milk": 3,
        "maple_syrup": 6,
        "pumpkin_spice": 6,
        "dark_chocolate": 5,
        "white_chocolate": 4
    },
    "latte": {
        "espresso": 5,
        "milk": 3,
        "sugar": 2,
        "vanilla": 4,
        "cinnamon": 5,
        "pumpkin_spice": 6,
        "honey": 4,
        "lavender": 5,
        "almond_milk": 3,
        "oat_milk": 3,
        "maple_syrup": 6
    },
    "mocha": {
        "espresso": 5,
        "milk": 3,
        "chocolate": 4,
        "sugar": 2,
        "dark_chocolate": 6,
        "white_chocolate": 5,
        "whipped_cream": 4,
        "caramel": 5,
        "hazelnut": 5
    },
    "fruit_tea": {
        "water": 1,
        "apple": 5,
        "honey": 4,
        "lemon": 5,
        "orange": 5,
        "strawberry": 6,
        "blueberry": 6,
        "raspberry": 7,
        "peach": 6,
        "pineapple": 7,
        "mango": 7,
        "passion_fruit": 8,
        "cherry": 6,
        "grape": 5,
        "cinnamon": 5,
        "ginger": 6,
        "mint": 4,
        "rose_petals": 5
    },
    }
    IDEAL_TEMPERATURES = {
        "tea": (70, 90),
        "coffee": (60, 80),
        "latte": (60, 70),
        "mocha": (60, 70),
        "fruit_tea": (70, 85),
    }

    def __init__(self, brew_type, name):
        self.type = brew_type
        self.name = name
        self.ingredients = []
        self.temperature = None
        self.score = 0
        self.waiting = False
        self.cooldown_count = 0
        self.flavor_profile = "regular"

    def add(self, ingredient):
        if ingredient in self.INGREDIENT_SCORES.get(self.type, {}):
            self.ingredients.append(ingredient)
            self.update_score(ingredient)
            print(f"Added {ingredient} to {self.name}")
        else:
            print(f"Ingredient {ingredient} is not valid for {self.type}.")

    def remove(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            self.update_score(ingredient, remove=True)
            print(f"Removed {ingredient} from {self.name}")
        else:
            print(f"{ingredient} is not in {self.name}")

    def heat(self, temperature):
        if temperature < 0 or temperature > 100:
            print("Temperature must be between 0 and 100 degrees Celsius.")
            return
        self.temperature = temperature
        if self.is_ideal_temperature():
            self.score += 5
            print(f"Heated {self.name} to {temperature}°C (Ideal!)")
        else:
            print(f"Heated {self.name} to {temperature}°C")
        self.waiting = True
        print("Waiting for the heat to settle...")
        time.sleep(3)
        self.waiting = False
        print(f"{self.name} is ready to proceed!")

    def stir(self):
        if self.waiting:
            print("Cannot stir while waiting for the temperature to settle!")
        else:
            print(f"Stirred {self.name}")
            self.score += 2

    def cooldown(self):
        if self.temperature and self.temperature > 20:
            self.temperature -= 10
            self.cooldown_count += 1
            print(f"{self.name} cooled down to {self.temperature}°C")
        else:
            print(f"{self.name} is already at room temperature or below!")

    def serve(self):
        if len(self.ingredients) == 0:
            print(f"You can't serve {self.name}, it has no ingredients!")
            return
        if "water" not in self.ingredients:
            print(f"{self.name} is missing its base ingredient (water)!")
            return

        ingredients = ", ".join(self.ingredients)
        temp = f" at {self.temperature}°C" if self.temperature else ""
        print(f"Served {self.name}: {ingredients}{temp}")
        print(f"Final Score: {self.score}")
        return self.score

    def inspect(self):
        ingredients = ", ".join(self.ingredients) if self.ingredients else "nothing"
        temp = f"{self.temperature}°C" if self.temperature else "not heated"
        cooldowns = f"{self.cooldown_count} times" if self.cooldown_count > 0 else "never"
        print(f"{self.name} contains: {ingredients}")
        print(f"Current temperature: {temp}")
        print(f"Cooldown applied: {cooldowns}")
        print(f"Current score: {self.score}")

    def gamble(self):
        outcome = random.choice(["win", "lose"])
        change = random.randint(5, 10)
        if outcome == "win":
            self.score += change
            print(f"You're lucky! Gained {change} points!")
        else:
            self.score -= change
            print(f"Bad luck... Lost {change} points.")

    def suggest(self):
        suggestions = {
            "tea": ["Add mint for a refreshing boost!", "Add honey for sweetness."],
            "coffee": ["Add chocolate for richness!", "Add vanilla for a luxurious taste."],
            "latte": ["Try adding a sprinkle of cinnamon!", "Add caramel for extra sweetness."],
            "mocha": ["Add whipped cream for a creamy finish!", "Try a dash of nutmeg."],
            "fruit_tea": ["Add more fruit for a vibrant flavor!", "Try a splash of lemon juice."],
        }
        if self.type in suggestions:
            print("Suggestion:", random.choice(suggestions[self.type]))
        else:
            print("Your drink is already perfect!")

    def recipe(self):
        recipes = {
            "tea": "To make a perfect tea, boil water, add tea leaves, steep for 3-5 minutes, and enjoy!",
            "coffee": "For a great coffee, brew espresso, add hot water, and mix with milk or cream.",
            "latte": "To prepare a latte, steam milk and pour it over a shot of espresso.",
            "mocha": "For a mocha, mix espresso with steamed milk and chocolate syrup, then top with whipped cream.",
            "fruit_tea": "To make fruit tea, steep tea with fresh fruits and honey for sweetness.",
        }
        if self.type in recipes:
            print("Recipe:", recipes[self.type])
        else:
            print("No recipe available for this type of brew.")

    def update_score(self, ingredient, remove=False):
        score_change = self.INGREDIENT_SCORES.get(self.type, {}).get(ingredient, 0)
        if remove:
            self.score -= score_change
        else:
            self.score += score_change
        if len(self.ingredients) > 5:
            print(f"Too many ingredients in {self.name}! The taste might be off.")
            self.score -= 2

    def is_ideal_temperature(self):
        if not self.temperature:
            return False
        ideal_range = self.IDEAL_TEMPERATURES.get(self.type, (0, 100))
        return ideal_range[0] <= self.temperature <= ideal_range[1]

    def seasonal_bonus(self):
        current_month = time.localtime().tm_mon
        if self.type == "mocha" and current_month in [11, 12, 1]:
            self.score += 5
            print("Seasonal bonus applied for winter mocha!")

    def weather_bonus(self, weather_condition):
        if weather_condition == "rainy":
            if "mint" in self.ingredients:
                self.score += 3
                print("Rainy day bonus for mint!")

    def taste_review(self):
        if self.score > 20:
            print("Expert review: Excellent!")
        elif self.score > 10:
            print("Expert review: Good!")
        else:
            print("Expert review: Needs improvement.")
