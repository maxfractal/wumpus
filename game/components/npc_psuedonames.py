import sys, random

print("Welcome to the NPC Name Generator.\n")
print("What will your companions name be?\n\n")

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
"Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
'Chewy','Chloe', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
'Katie','Lemongrass', 'Lil Debil','Liz', 'Longbranch', '"Lunch Money"',
'Max','Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
"Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
"Winston 'Jazz Hands'", 'Worms')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
'Hootkins','Johnson', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
'Oxhandler', 'Parsell','Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
'Woolysocks')

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)

    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")

    try_again = input("Try again? (Press enter or n to quit)\n ")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")