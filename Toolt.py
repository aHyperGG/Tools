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
        print("Hello")
        #print("LETS GOOO BEACUSE IM ", hotness()"!!")
    elif ready.lower == "no":
        print("ok")
        #ready = input("Tell me when your ready cause "hotness()" ex:just write out ready!")
    else:
        while ready.lower != "yes" or "no":
            print("Please enter a valid answer! eg: yes or no!!")
    print("You have 10 seconds to open the window with the auth to crack!!!!!! LETS GOOOOOOOOOOOO!!!!!!!!!!!")
    print("Press any letter to skip 1 second")
    wait(10)
    input("")
