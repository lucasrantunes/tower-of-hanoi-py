from game import Game
print("Choose one option:")
print(" 1) Start Game")
print(" 2) Exit")


while True:

    user_input = int(input())
    if user_input == 1:
        g = Game(3)
    elif user_input == 2:
        print("Exit")
    else:
        print("Insert a valid option.")