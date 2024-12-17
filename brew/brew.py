from brew.ingredients import INGREDIENT_SCORES
from brew.temperature import IDEAL_TEMPERATURES
from brew.brew_utils import update_score
from brew.brew_utils import is_ideal_temperature
import time
import random

class Brew:
    def __init__(self, brew_type, name):
        self.type = brew_type
        self.name = name
        self.ingredients = []
        self.temperature = None
        self.score = 0
        self.waiting = False
        self.cooldown_count = 0
        self.flavor_profile = "regular"
        self.weather_bonus_applied = False
        self.seasonal_bonus_applied = False

    def add(self, ingredient):
        if ingredient in INGREDIENT_SCORES.get(self.type, {}):
            self.ingredients.append(ingredient)
            update_score(self, ingredient)
            print(f"Added {ingredient} to {self.name}")
        else:
            print(f"Ingredient {ingredient} is not valid for {self.type}.")

    def remove(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            update_score(self, ingredient, remove=True)
            print(f"Removed {ingredient} from {self.name}")
        else:
            print(f"{ingredient} is not in {self.name}")

    def heat(self, temperature):
        if temperature < 0 or temperature > 100:
            print("Temperature must be between 0 and 100 degrees Celsius.")
            return
        self.temperature = temperature
        if is_ideal_temperature(self):
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
            "coffee": "For a great coffee, brew espresso, add hot water, and mix with milk or cream as desired.",
            "latte": "To prepare a latte, steam milk and pour it over a shot of espresso.",
            "mocha": "For a mocha, mix espresso with steamed milk and chocolate syrup.",
            "fruit_tea": "To create fruit tea, steep tea with fresh fruits and sweeten to taste.",
        }
        if self.type in recipes:
            print("Recipe:", recipes[self.type])
        else:
            print("No recipe available for this drink type.")

    def weather_bonus(self, condition):
        bonus_ranges = {
            "sunny": (3, 7),
            "rainy": (5, 15),
            "snowy": (4, 12),
            "cloudy": (1, 4)
        }

        if self.weather_bonus_applied:
            print(f"Weather bonus has already been applied to {self.name}.")
            return

        if condition in bonus_ranges:
            min_bonus, max_bonus = bonus_ranges[condition]
            bonus_value = random.randint(min_bonus, max_bonus) 
            self.score += bonus_value
            self.weather_bonus_applied = True 
            print(f"Applied weather bonus of {bonus_value} to {self.name} due to {condition} weather.")
        else:
            print(f"No bonus defined for weather condition: {condition}.")

    def seasonal_bonus(self, season):
        bonus_ranges = {
            "spring": (3, 8),
            "summer": (5, 12),
            "autumn": (2, 6),
            "winter": (1, 5)
        }

        if self.seasonal_bonus_applied:
            print(f"Seasonal bonus has already been applied to {self.name}.")
            return

        if season in bonus_ranges:
            min_bonus, max_bonus = bonus_ranges[season]
            bonus_value = random.randint(min_bonus, max_bonus)
            self.score += bonus_value
            self.seasonal_bonus_applied = True
            print(f"Applied seasonal bonus of {bonus_value} to {self.name} due to {season} season.")
        else:
            print(f"No bonus defined for season: {season}.")

    def taste_review(self):
        if self.score > 20:
            print("Expert review: Excellent!")
        elif self.score > 10:
            print("Expert review: Good!")
        else:
            print("Expert review: Needs improvement.")
