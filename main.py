print("Choose one option:")
print(" 1) Start Game")
print(" 2) Exit")


while True:
    try:
        user_input = int(input())
        if user_input == 1:
            print("Start.")
        elif user_input == 2:
            print("Exit")
        else:
            print("Insert a valid option.")
    except:
        print("Insert a valid input.")