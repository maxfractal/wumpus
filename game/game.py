#copied from game3 into this file 05172026
from player import Player
import world

def play():
    print("Escape from Cave Terror!")
    player = Player()
    while True:
        room = world.tile_at(player.x,player.y)
        print(room.intro_text())
        room.modify_player(player) #new line
        action_input = get_player_command().strip().lower()
        if action_input in ['n','north']:
            move_player(player, 0, -1)
        elif action_input in ['s','south']:
            move_player(player, 0, 1)
        elif action_input in ['e','east']:
            move_player(player, 1, 0)
        elif action_input in ['w','west']:
            move_player(player, -1, 0)
        elif action_input in ['i','inventory']:
            player.print_inventory()
        elif action_input in ['a','attack']:
            player.attack()
        elif action_input in ['m','map','location']:
            print_player_location(player)
        elif action_input in ['q','quit']:
            print('Bye! Come back to the cave soon!')
            exit()
        else:
            print("Invalid action!")
            print('Bye!')
            exit()

def get_player_command():
        return input('Action: ')

def move_player(player, dx, dy):
    new_x = player.x + dx
    new_y = player.y + dy
    if world.tile_at(new_x, new_y) is None:
        print("You can't go that way.")
        return
    player.move(dx, dy)

def print_player_location(player):
    for y, row in enumerate(world.world_map):
        map_row = []
        for x, tile in enumerate(row):
            if player.x == x and player.y == y:
                map_row.append("P")
            elif tile is None:
                map_row.append(" ")
            else:
                map_row.append(".")
        print(" ".join(map_row))

play()
