#!/Users/xris/opt/anaconda3/bin/python

""" Hunt the wumpus! """

from random import choice

cave_numbers = range(1,21)
"""
wumpus_location = choice(cave_numbers)
wumpus_friend_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while (player_location == wumpus_location or 
        player_location == wumpus_friend_location):
    player_location = choice(cave_numbers)




"""
caves = [];
print(caves);
print("___test____");
#for i in cave_numbers:
#    caves.append([])



"""
#Connecting caves    
#set up
#changing unvisited_caves to a list
#to make it work
unvisited_caves = list(range(0, 20));
visited_caves = [0];
unvisited_caves.remove(0);

#main loop
#replacing section 4 and 5 pg.47
print ("You are in a cave", player_location);
print ("From here, you can see caves:", caves[player_location]);
if wumpus_location in caves[player_location]:
    print ("I smell a wumpus!");

while unvisited_caves != []:
    i = choice(visited_caves)
    if len(caves[i]) >= 3:
        continue

    next_cave = choice(unvisited_caves)
    caves[i].append(next_cave)
    caves[next_cave].append(i)

    visited_caves.append(next_cave)
    unvisited_caves.remove(next_cave)

    for number in cave_numbers:
        print(number, ":", caves[number]);
    print('------------');

    for i in cave_numbers:
        while len(caves[i]) < 3:
            passage_to = choice(cave_numbers)
            caves[i].append(passage_to)

    for number in cave_numbers:
        print (number, ":", caves[number]);
        print('------------');
#end connecting caves

#I have no idea is this next section stays or not.
for i in cave_numbers:
    for j in range(3):
        passage_to = choice(cave_numbers)
        caves[i].append(passage_to)
print(caves);
"""

wumpus_location = choice(cave_numbers)
wumpus_friend_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while (player_location == wumpus_location or
    player_location == wumpus_friend_location):
    player_location = choice(cave_numbers)

print ("Welcome to Hunt the Wumpus!");
print ("You can see ", len(cave_numbers), " caves.");
print ("To play, just type the number");
print ("of the cave you wish to enter next.");

while 1:
    print ("You are in a cave", player_location);
    #print ("From here, you can see caves:", caves[player_location]);
    if (player_location == wumpus_location - 1 or
    player_location == wumpus_location + 1):
    # in caves[player_location]:
        print ("I smell a wumpus...");
    if (player_location == wumpus_friend_location - 1 or
        player_location == wumpus_friend_location + 1):
        print ("I smell an even stinkier wumpus!");

    print ("Which cave next?");
    player_input = input(">")
    if (not player_input.isdigit() or
        #int(player_input) not in caves[player_location]):
        int(player_input) not in cave_numbers):
            print (player_input + "?");
            #print (player_input, " is not a cave!");
            print ("That's not a direction that I can see!");
            continue

    else: 
        player_location = int(player_input)
        if player_location == wumpus_location:
            print ("Aargh! You got hugged by a wumpus!");
            break
        if player_location == wumpus_friend_location:
            print ("Aargh! You got eaten by the wumpus' friend wumpus!");
            break
