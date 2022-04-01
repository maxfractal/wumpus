from foo import *
import subprocess

print("start");
print(first_three);
print("  from f003  ");
print(last_three);
subprocess.call("./foo2.sh", shell=True);
wumpus_r_us_list.append('Rope');
print (wumpus_r_us_list);

#TODO
#Create a list of contents to the prompt
wumpus_r_us_list.remove('Rope');
print(wumpus_r_us_list);
print("Wumpus hunting checklist:");
for each_item in wumpus_r_us_list:
    print(each_item);
    if each_item == "Lantern":
        print ("Don't forget to light your lantern");
        print ("once you're down there.");
print("end.");