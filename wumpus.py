from random import choice

cave_numbers = range(0,20)
caves = []
for i in cave_numbers:
    caves.append([])

for i in cave_numbers:
    for j in range(3):
        passage_to = choice(cave_numbers)
        caves[i].append(passage_to)
print(caves);

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

while True:
    print ("You are in a cave", player_location);
    if (player_location == wumpus_location - 1 or
        player_location == wumpus_location + 1):
        print ("I smell a wumpus...");
    if (player_location == wumpus_friend_location - 1 or
        player_location == wumpus_friend_location + 1):
        print ("I smell an even stinkier wumpus!");

    print ("Which cave next?");
    player_input = input(">")
    if (not player_input.isdigit() or
        int(player_input) not in [player_location]):
        print player_input + "?";
        print (player_input, " is not a cave!");

    else: 
        player_location = int(player_input)
        if player_location == wumpus_location:
            print ("Aargh! You got hugged by a wumpus!");
            break
        if player_location == wumpus_friend_location:
            print ("Aargh! You got eaten by the wumpus' friend wumpus!");
            break
