#this version is like the book at this point
from player import Player

def play():
    print("Escape from Cave Terror!")
    player = Player()
    while True:
        action_input = get_player_command()
        if action_input in ['n','N','north','North']:
            print("Go North!")
        elif action_input in ['s','S','south','South']:
            print("Go South!")
        elif action_input in ['e','E','east','East']:
            print("Go East!")
        elif action_input in ['w','W','west','West']:
            print("Go West!")
        elif action_input in ['i','I','inventory','Inventory']:
            player.print_inventory()
        else:
            print("Invalid action!")
            print('Bye!')
            exit()

def get_player_command():
        return input('Action: ')

play()
