from weapons import *


def play():
    inventory = [Rock(), 'Gold(5)', 'Crusty Bread']
    print("Escape from Cave Terror")
    while True:
        action_input = get_player_command()
        if action_input in ['n','N','north','Nouth']:
            print("Go North!")
        elif action_input in ['s','S','south','South']:
            print("Go South!")
        elif action_input in ['e','E','east','East']:
            print("Go East!")
        elif action_input in ['w','W','west','West']:
            print("Go West!")
        elif action_input in ['i','I','inventory','Inventory']:
            print("Inventory:")
            #print(inventory)
            for item in inventory:
                print('*' + str(item))
        else:
            print("Invalid action!")
            print('Bye!')
            exit()

def get_player_command():
        return input('Action: ')

play()