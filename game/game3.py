#this version is like the book at this point
from player import Player
import world

def play():
    print("Escape from Cave Terror!")
    player = Player()
    while True:
        room = world.tile_at(player.x,player.y)
        print(room.intro_text())
        action_input = get_player_command()
        if action_input in ['n','N','north','North']:
            player.move_north
        elif action_input in ['s','S','south','South']:
            player.move_south
        elif action_input in ['e','E','east','East']:
            player.move_east
        elif action_input in ['w','W','west','West']:
            player.move_west
        elif action_input in ['i','I','inventory','Inventory']:
            player.print_inventory()
        elif action_input in ['q','Q','quit','Quit']:
            print('Bye! Come back to the cave soon!')
            exit()
        else:
            print("Invalid action!")
            print('Bye!')
            exit()

def get_player_command():
        return input('Action: ')

play()
