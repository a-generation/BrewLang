from brew.brew import Brew
from commands import process_command

class BrewInterpreter:
    def __init__(self):
        self.brews = {}
        self.current_brew = None

    def run(self):
        while True:
            command = input("> ")
            if process_command(command, self) == "exit":
                break
