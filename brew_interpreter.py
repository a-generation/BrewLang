from brew import Brew

class BrewInterpreter:
    def __init__(self):
        self.brews = {}
        self.current_brew = None

    def process_command(self, command):
        parts = command.split()
        if not parts:
            return

        cmd = parts[0]

        if cmd == "setbrew":
            if len(parts) < 3:
                print("Usage: setbrew <tea/coffee/latte/mocha/fruit_tea> <name>")
                return
            brew_type, name = parts[1], parts[2]
            if brew_type not in Brew.INGREDIENT_SCORES.keys():
                print("Only 'tea', 'coffee', 'latte', 'mocha', or 'fruit_tea' types are supported!")
                return
            self.brews[name] = Brew(brew_type, name)
            print(f"Brewing {brew_type}: {name}")

        elif cmd == "selectbrew":
            if len(parts) < 2:
                print("Usage: selectbrew <name>")
                return
            name = parts[1]
            if name in self.brews:
                self.current_brew = self.brews[name]
                print(f"Selected {name}")
            else:
                print(f"B rew {name} not found!")

        elif cmd == "add":
            if len(parts) < 2:
                print("Usage: add <ingredient>")
                return
            ingredient = " ".join(parts[1:])
            if self.current_brew:
                self.current_brew.add(ingredient)
            else:
                print("No brew selected! Use 'selectbrew <name>' to select a brew.")

        elif cmd == "remove":
            if len(parts) < 2:
                print("Usage: remove <ingredient>")
                return
            ingredient = " ".join(parts[1:])
            if self.current_brew:
                self.current_brew.remove(ingredient)
            else:
                print("No brew selected! Use 'selectbrew <name>' to select a brew.")

        elif cmd == "heat":
            if len(parts) < 2:
                print("Usage: heat <temperature>")
                return
            try:
                temperature = int(parts[1])
                if self.current_brew:
                    self.current_brew.heat(temperature)
                else:
                    print("No brew selected! Use 'selectbrew <name>' to select a brew.")
            except ValueError:
                print("Temperature must be an integer!")

        elif cmd == "stir":
            if self.current_brew:
                self.current_brew.stir()
            else:
                print("No brew selected! Use 'selectbrew <name>' to select a brew.")

        elif cmd == "cooldown":
            if self.current_brew:
                self.current_brew.cooldown()
            else:
                print("No brew selected! Use 'selectbrew <name>' to select a brew.")

        elif cmd == "gamble":
            if self.current_brew:
                self.current_brew.gamble()
            else:
                print("No brew selected! Use 'selectbrew <name>' to select a brew.")

        elif cmd == "suggest":
            if self.current_brew:
                self.current_brew.suggest()
            else:
                print("No brew selected! Use 'selectbrew <name>' to select a brew.")

        elif cmd == "inspect":
            if self.current_brew:
                self.current_brew.inspect()
            else:
                print("No brew selected! Use 'selectbrew <name>' to select a brew.")

        elif cmd == "serve":
            if self.current_brew:
                final_score = self.current_brew.serve()
                del self.brews[self.current_brew.name]
                self.current_brew = None
                print(f"Final brew score: {final_score}")
            else:
                print("No brew selected! Use 'selectbrew <name>' to select a brew.")

        elif cmd == "seasonal_bonus":
            if self.current_brew:
                self.current_brew.seasonal_bonus()
            else:
                print("No brew selected! Use 'selectbrew <name>' to select a brew.")

        elif cmd == "weather_bonus":
            if len(parts) < 2:
                print("Usage: weather_bonus <condition>")
                return
            weather_condition = parts[1]
            if self.current_brew:
                self.current_brew.weather_bonus(weather_condition)
            else:
                print("No brew selected! Use 'selectbrew <name>' to select a brew.")

        elif cmd == "taste_review":
            if self.current_brew:
                self.current_brew.taste_review()
            else:
                print("No brew selected! Use 'selectbrew <name>' to select a brew.")

        elif cmd == "recipe":
            if self.current_brew:
                self.current_brew.recipe()
            else:
                print("No brew selected! Use 'selectbrew <name>' to select a brew.")

        elif cmd == "exit":
            print("Exiting Brew Interpreter. Goodbye!")
            return "exit"

        else:
            print(f"Unknown command: {cmd}")
