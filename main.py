from brew_interpreter import BrewInterpreter
from commands import process_command

def main():
    print("Welcome to the Brew Interpreter! (1.1-28-sapling)")
    print("Type 'exit' to quit.")
    print("Available commands:")
    print("  setbrew <tea/coffee/latte/mocha/fruit_tea> <name> - Create a new brew")
    print("  selectbrew <name>                                   - Select an existing brew")
    print("  add <ingredient>                                    - Add an ingredient to the selected brew")
    print("  remove <ingredient>                                 - Remove an ingredient from the selected brew")
    print("  heat <temperature>                                  - Heat the selected brew to a temperature")
    print("  stir                                                - Stir the selected brew")
    print("  cooldown                                            - Cool down the brew")
    print("  gamble                                              - Gamble points")
    print("  suggest                                             - Get suggestions to improve the brew")
    print("  inspect                                             - Inspect the current brew")
    print("  serve                                               - Serve the selected brew print")
    print("  seasonal_bonus <season>                             - Apply seasonal bonus to the selected brew based on season")
    print("  weather_bonus <condition>                           - Apply weather bonus based on condition")
    print("  taste_review                                        - Get expert review of the selected brew")
    print("  recipe                                              - Get recipe for the selected brew")
    print("  exit                                                - Quit the interpreter")
    print()

    interpreter = BrewInterpreter()

    while True:
        command = input("> ")
        if process_command(command, interpreter) == "exit":
            break


if __name__ == "__main__":
    main()
