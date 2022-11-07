# My tools!
import os
import time
import hoting

#Ping Sweeping!
def pingsweep():
	is_prefix = input("Is the ip prefix 192.168?: ")
    while is_prefix.lower != null:
        if is_prefix.lower == "yes":
                prefix = is_prefix
                break
        elif is_prefix.lower == "no":
            is_prefix = input("Please Enter the prefix of the ip address: ")
            is_prefix = prefix
            break
        else:
            print("Please Enter a valid answer ex: yes or no")
    ping(prefix)
    ping(is_prefix)
# To be continued

#BruteForcing!

def BruteForcer():
    Hello = input("Hello Welcome to my bruteforcing program! Do you have a list?: ")
    if Hello.lower == "yes":
        file_path = input("Please enter the path of the file: ")
    elif Hello.lower == "no":
        print("Its Okay no worries, for now i haven't coded this part of the progrom sorry!, i suggest you come back with a list, bye! Have a nice Day!")
    file = open(file_path, r)
    list = (file.read())
    ready = input("Ready?")
    if ready.lower == "yes":
        print("LETS GOOO BEACUSE IM "hotness()"!!")
    elif ready.lower == "no":
        ready = input("Tell me when your ready cause "hotness()" ex:just write out ready!")
    else:
        while ready.lower != "yes" or "no"
            print("Please enter a valid answer! eg: yes or no!!")
    print("You have 10 seconds to open the window with the auth to crack!!!!!! LETS GOOOOOOOOOOOO!!!!!!!!!!!")
    print("Press any letter to skip 1 second")
    wait(10)
    key.input("")