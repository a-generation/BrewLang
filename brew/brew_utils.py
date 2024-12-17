from brew.temperature import IDEAL_TEMPERATURES
from brew.ingredients import INGREDIENT_SCORES

def update_score(self, ingredient, remove=False):
    if remove:
        self.score -= INGREDIENT_SCORES[self.type][ingredient]
    else:
        self.score += INGREDIENT_SCORES[self.type][ingredient]

def is_ideal_temperature(self):
    ideal_range = IDEAL_TEMPERATURES.get(self.type, (0, 100))
    return ideal_range[0] <= self.temperature <= ideal_range[1]
