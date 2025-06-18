# Snake-Water-Gun Game

"""
Game Description :-
Snake Water Gun is a fun and simple two-player game similar to Rock Paper Scissors,
where each player (or player vs computer) chooses one of the three options: Snake, Water, or Gun.
The outcome is determined based on a fixed set of rules.

Rules :-
Snake drinks Water → Snake wins
Water drowns Gun → Water wins
Gun kills Snake → Gun wins
If both players choose the same, it's a draw

Here, the game mode is Computer VS Player
where, first computer selects its choice randomly which is hidden initially, and then asks for your choice
then out is desided, by showing the choices of both parties.
"""


import time
import random

print("Welcome To The Game,     💧   🔫  🐍 \n                    THE WATER-GUN-SNAKE\n")
name = input("Enter Your Name : ")
print("\nHello",name,"Let's Begin The Game")
print("You Have 10 Iterations To Play The Game")
print("Your Game Is Being Started",end="")

#--------------------------loader---------------------------
for i in range(0,10) :
    time.sleep(0.25)
    print(".", end=" ")
print("\n")
print("Enter :\n1 For Snake 🐍\n2 For Water 💧\n3 For Gun 🔫\n")

#-----------------------------------------------------------

dic = {1 : "Snake 🐍", 2 : "Water💧", 3 : "Gun 🔫"}

w = 0
d = 0
l = 0
lbreak = False

for i in range(10) :
#----------------taking random input from system------------
    sys = random.randint(1, 3)


#----------------error handelling in user input--------------

    k = 0
    while True :
        try :   
            user = int(input("Select Your Choice : "))
            if (user != 1 and user != 2 and user != 3) :
                raise ValueError

        except ValueError :
            print("\t\tINVALID INPUT")
            if k < 2 :
                print("Please Select Out Of 1, 2 and 3 Only")
                k += 1
                continue
            else :
                print("You Have Been Eliminated From The Game Due To Too Much Of Wrong Entries")
                lbreak = True
                break
        else :
#---------------------evaluating user input-----------------

            if sys == 1 :
                    print("System Has Selected", dic[1])
            elif sys == 2 :
                print("System Has Selected", dic[2])
            else :
                print("System Has Selected", dic[3])

            print("You have Selected",dic[user])

            if sys == user :
                print("\t\tDRAW 🟰")
                d += 1
            elif (sys == 2 and user == 1) or (sys == 3 and user == 2) or (sys == 1 and user == 3) :
                print("\t\tYOU WIN ✔️")
                w += 1
            else  :
                print("\t\tYOU LOSE ❌")
                l += 1
    
            break
    if lbreak == True :
        break

#-------------------evaluating final score------------------

print("\n\t\tGame Over!!!\n\n\t\tYour Stats :-",sep="")
print("\t\tYou Encountered\n\t\t",w," Wins\n\t\t",d," Draws\n\t\t",l," Losses",sep="")

