#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations
#to the winner, and ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock
import random
import time
r="rock"
s="scissors"
p="paper"

def who_is_winner():# Decides who is winner
    time.sleep(2)
    choise=str(input("Choose betwer rock, scissors and paper(use lower case):  "))
    if choise==r or choise==s or choise==p:
        timer_funny()
    else:
        print("Type your choise correctly, my lord!! Try again")
        who_is_winner()#If didnt type correctly
    bots_choise=random.randint(0,2)# randomize bots choise
    if bots_choise==0:
        bots_choise=r
    elif bots_choise==1:
        bots_choise=s
    elif bots_choise==2:
        bots_choise=p
    if choise==r and bots_choise==s or choise==s and bots_choise==p or choise==p and bots_choise==r:#Users win condition
        print("You won!! Your type was ",choise," and bot choose ",bots_choise,"\n")
        game()
    elif bots_choise==r and choise==s or bots_choise==s and choise==p or bots_choise==p and choise==r:#Bots win conditions
        print("You lost :'( Your type was ",choise," and bot choose ",bots_choise,"\n")
        game()
    elif choise==bots_choise:
        print("It's a tie! Lets play again...\n")
        who_is_winner() #If its a tie
        
def timer_funny():# Count just for fun
    print("So.. Lets play... my lord...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GOO~!!!!\n")

def game():#main func
    while True:
        usr_command = input("Enter your command(type 'quit' to exit): ")
        if usr_command == "quit":
            break
        else: 
            print("You chose to " + usr_command)
            who_is_winner()
game()  
