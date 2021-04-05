"""
Author: Luke Carlson
This program allows you to play chutes and ladders against the computer in your terminal window
"""
import random
end = 0 #If ends = 1 the program knows the game is over
eq = 0 #If eq = 1 the program knows the user quit early
round = 1 #Round starts at one and continuously increases
spaces0 = 50 #Spaces for Siri
spaces1 = 50 #Spaces for player 1
print ("------------------------------\nWelcome to Dice Race!!!\nHuman vs Machine\n------------------------------ ")
p1 = input("Who is player 1? ") #Accept the users name

while (end != ""): #Keep asking the player to hit enter until they do
    end = input("Press ENTER to begin")

while(end != 1 and spaces0 > 0 and spaces1 > 0): #This continuously loops the game until someone wins
    print("\n----- Round ", round, " -----\nSiri rolled the dice.")
    round = round + 1
    dice1 = random.randint(1,6) #This sets two dice for the user to roll
    dice2 = random.randint(1,6)
    print("Siri rolled a", dice1, "and a", dice2)
    spaces0 = spaces0 - (dice1 + dice2)

    #CorQ 'stands for Continue or Quit'
    CorQ = input("Press ENTER to continue playing with Siri (0 to quit): ") #Lets the player quit early
    while (CorQ != ""):
        if (CorQ == "0"):
            print ("Thanks for playing!!!")
            end = 1
            eq = 1 #Makes python aware the user has quit early
            break
        else:
            CorQ = input("Press ENTER to continue playing with Siri (0 to quit): ")

    if (end != 1):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("\nYou rolled a", dice1, "and a", dice2)
        spaces1 = spaces1 - (dice1 + dice2)
        print(p1, "you still have ", spaces1, " spaces left to finish")

        if(spaces1 == 39 or spaces1 == 28 or spaces1 == 17 or spaces1 == 6):#THESE ARE STILL THE MULTIPLES OF 11, JUST MODIFIED FOR DESCENDING ORDER
            print("----- BUT-----\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print(p1, "just hit a chute!")
            print(p1, "has to go back to the beginning")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            spaces1 = 50
        if(spaces0 == 39 or spaces0 == 28 or spaces0 == 17 or spaces0 == 6): #THESE ARE STILL THE MULTIPLES OF 11, JUST MODIFIED FOR DESCENDING ORDER
            print("----- BUT-----\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("Siri just hit a chute!")
            print("Siri has to go back to the beginning")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            spaces0 = 50
        sp1 = (spaces1 - 50) * -1 #I made the spaces in descending order, this reverses them for progress recording
        sp0 = (spaces0 - 50) * -1
        print (p1, "you have moved", sp1, "spaces")
        print ("Siri has moved", sp0, "spaces")
else:
    print("---------------------------------------------------\n\n\n") #Gives a line to seperate the endgame
    if (eq == 1):
        print("You have quit early, Siri wins, try again next time")
    elif (spaces0 < spaces1):
        print("Siri has won, better luck next time!!!")
    elif (spaces0 == spaces1):
        print("While Siri technically finished first, on your last roll you tied with her!!!")
    elif (spaces0 > spaces1):
        print("Congratulations, you have won!!!")
