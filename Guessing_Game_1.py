#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

#Extras:
#Keep the game going until the user types �exit�
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
loss=0
win=1
score_list=[]


def score(point):#score func
    if point==0:
        score_list.append(0)
    elif point==1:
        score_list.append(1)
    elif point==2:
        print("\nYour score is ",sum(score_list)," out of ",(len(score_list)))          
def setlimits():#chosing the limits
    global lowlimit
    global highlimit
    lowlimit=int(input("Type the lower limit: "))
    highlimit=int(input("Type the higher limit: "))
    print("Okay the limits are now ",lowlimit," to ",highlimit)
    main()   
def guess(prog, user):#guessing func
    if user<prog:
        print("\nIts lower than i imagined! I imagined ",prog)
        score(loss)
    elif user>prog:
        print("\nIts higher than i imagined!I imagined ",prog)
        score(loss)
    elif user==prog:
        print ("\nIts exatctly what i imagined! How did u do that?!") 
        score(win)
def main():
    randnum=random.randint(lowlimit,highlimit)
    list_of_numbers=list(range(lowlimit,highlimit+1)) 
    users_number=input("Guess a number, type it and press Enter(or type 'set' to set the limits): ")
    if users_number=="exit":# Exit
            print("\nYou choose to exit. Your final score is: \n")
            score(2)
            input("Press Enter to continue...")
            exit()
    elif users_number=="set":
        setlimits()
    else:
            if int(users_number) not in list_of_numbers:
                print("Wrong input :( Try again. We play only betwen 1 and 9")
                main()
            else:#starting the game if everything is okay
                guess(randnum,int(users_number))
                score(2)
                main()   
setlimits()  
main()
