from brew.brew import Brew

def process_command(command, interpreter):
    parts = command.split()
    if not parts:
        return

    cmd = parts[0]
    
    if cmd == "setbrew":
        if len(parts) < 3:
            print("Usage: setbrew <type> <name>")
            return
        brew_type = parts[1]
        name = ' '.join(parts[2:])  # Объединяем все части имени
        if name.startswith('"') and name.endswith('"'):
            name = name[1:-1]  # Убираем кавычки
        elif name.startswith("'") and name.endswith("'"):
            name = name[1:-1]  # Убираем кавычки
        interpreter.current_brew = Brew(brew_type, name)
        interpreter.brews[name] = interpreter.current_brew
        print(f"Set current brew to {name} of type {brew_type}.")
    
    elif cmd == "selectbrew":
        if len(parts) < 2:
            print("Usage: selectbrew <name>")
            return
        name = ' '.join(parts[1:])  # Объединяем все части имени
        if name.startswith('"') and name.endswith('"'):
            name = name[1:-1]  # Убираем кавычки
        elif name.startswith("'") and name.endswith("'"):
            name = name[1:-1]  # Убираем кавычки
        if name in interpreter.brews:
            interpreter.current_brew = interpreter.brews[name]
            print(f"Selected brew: {name}.")
        else:
            print(f"Brew {name} not found.")
    
    elif cmd == "add":
        if interpreter.current_brew is None:
            print("No brew selected.")
            return
        if len(parts) < 2:
            print("Usage: add <ingredient>")
            return
        ingredient = parts[1]
        interpreter.current_brew.add(ingredient)
    
    elif cmd == "remove":
        if interpreter.current_brew is None:
            print("No brew selected.")
            return
        if len(parts) < 2:
            print("Usage: remove <ingredient>")
            return
        ingredient = parts[1]
        interpreter.current_brew.remove(ingredient)
    
    elif cmd == "heat":
        if interpreter.current_brew is None:
            print("No brew selected.")
            return
        if len(parts) < 2:
            print("Usage: heat <temperature>")
            return
        try:
            temperature = int(parts[1])
            interpreter.current_brew.heat(temperature)
        except ValueError:
            print("Temperature must be a number.")
    
    elif cmd == "stir":
        if interpreter.current_brew is None:
            print("No brew selected.")
            return
        interpreter.current_brew.stir()
    
    elif cmd == "cooldown":
        if interpreter.current_brew is None:
            print("No brew selected.")
            return
        interpreter.current_brew.cooldown()
    
    elif cmd == "serve":
        if interpreter.current_brew is None:
            print("No brew selected.")
            return
        interpreter.current_brew.serve()
    
    elif cmd == "inspect":
        if interpreter.current_brew is None:
            print("No brew selected.")
            return
        interpreter.current_brew.inspect()
    
    elif cmd == "gamble":
        if interpreter.current_brew is None:
            print("No brew selected.")
            return
        interpreter.current_brew.gamble()
    
    elif cmd == "suggest":
        if interpreter.current_brew is None:
            print("No brew selected.")
            return
        interpreter.current_brew.suggest()
    
    elif cmd == "recipe":
        if interpreter.current_brew is None:
            print("No brew selected.")
            return
        interpreter.current_brew.recipe()
    
    elif cmd == "weather_bonus":
        if len(parts) < 2:
            print("Usage: weather_bonus <condition>")
            return
        condition = parts[1]
        if interpreter.current_brew is None:
            print("No brew selected.")
            return
        interpreter.current_brew.weather_bonus(condition)

    elif cmd == "taste_review":
        if interpreter.current_brew:
            interpreter.current_brew.taste_review()
        else:
            print("No brew selected! Use 'selectbrew <name>' to select a brew.")

    elif cmd == "seasonal_bonus":
        if len(parts) < 2:
            print("Usage: seasonal_bonus <season>")
            return
        season = parts[1]
        if interpreter.current_brew is None:
            print("No brew selected.")
        else:
            interpreter.current_brew.seasonal_bonus(season)

    elif cmd == "exit":
        return "exit"
    
    else:
        print(f"Unknown command: {cmd}")
