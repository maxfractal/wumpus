shopping_list = ['Milk','Bread','I killed a man once','Cheese','Squid Game']
wumpus_r_us_list = ["Bow and Arrow","Lantern","Wumpus repellant"]
my_shoppping_lists = [shopping_list,wumpus_r_us_list]

print(shopping_list);
print(shopping_list[0]);
print(shopping_list[-1]);
print(my_shoppping_lists);

wumpus_r_us_list.append('Rope');

first_three = wumpus_r_us_list[:3]
last_three = wumpus_r_us_list[1:]
print(my_shoppping_lists);

if 'Milk' in shopping_list:
    print("Oh good you brought Milk for the Squid games.");

print(first_three);
print("    ");
print(last_three);