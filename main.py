from rich import print
from game import Game

user_desire = True
while user_desire:

    print("\nType [bold blue]start[/bold blue] to star game or [bold red]exit[/bold red] to quit game: ")
    user_input = input()
    if user_input == "start":
        g = Game(4)
    elif user_input == "exit":
        user_desire = False
    else:
        print("[red]Insert a valid option.[/red]")