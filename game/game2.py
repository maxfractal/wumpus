#this version is like the book at this point
class Weapon:
    def __str__(self):
        return self.name

class Rock:
    def __init__(self):
        self.name = "Rocky the rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5

    def __str__(self):
        return self.name
    
class Dagger:
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. "  "Somewhat more dangerous than a rock."
        self.damage = 10

    def __str__(self):
        return self.name
    
class RustySword:
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing its age, " "but still has some fight left in it."
        self.damage = 20

    def __str__(self):
        return self.name


def play():
    inventory = [Rock().name, 'Gold(5)', 'Crusty Bread']
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