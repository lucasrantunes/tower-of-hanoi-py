from game import Game

user_desire = True
while user_desire:

    user_input = input("\nType 'start' to star game or 'exit' to quit game: ")
    if user_input == "start":
        g = Game(4)
    elif user_input == "exit":
        user_desire = False
    else:
        print("Insert a valid option.")