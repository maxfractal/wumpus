#this version is like the book at this point
import weapons


r1 = weapons.Rock("A fist-sized rock, suitable for bludgeoning.",5)
d1 = weapons.Dagger()

def play():
    inventory = [r1.name, d1.name, 'Gold(5)', 'Crusty Bread']
    print("Escape from Cave Terror")
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