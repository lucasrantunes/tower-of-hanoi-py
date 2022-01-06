from stack import Stack
from controller import Controller


class Game:
    def __init__(self, difficulty):
        print("Type 'back' if you want to go back to main menu.")
        self.difficulty = difficulty
        self.stacks = [Stack(difficulty), Stack(), Stack()]
        self.controller = Controller()

        user_desire = True
        while user_desire:
            user_desire = self.__get_user_command()
        

    def __get_user_command(self) -> bool:
        try:
            user_input = input("Insert moviment: ")
            print(user_input)
            if user_input == "back": 
                return False
            else:
                user_input = user_input.split(" ")
                current_stack = int(user_input[0])
                target_stack = int(user_input[1])

                if (current_stack >= 1 and current_stack <= 3) and (target_stack >= 1 and target_stack <= 3):
                    self.controller.move_disk(self.stacks, current_stack - 1, target_stack - 1)
                    return True
        except:
            print("Insert a valid input [0].")
            return True
