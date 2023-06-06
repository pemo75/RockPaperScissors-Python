# simple Rock-Paper-Scissors code
# programmer : Pegah Moslemi

import random
score = 0

while True:
    print("Your Score: " + str(score))
    choice = input("1- Rock \n2- paper \n3- Scissors \n(0 -> Exit) \n")
    choice = int(choice)

    if choice!=1 and choice!=2 and choice!=3 and choice!=0 :
        print("invalid input! Try again: ")
        print("Your Score: " + str(score))
        choice = input("1- Rock \n2- paper \n3- Scissors \n")
        choice = int(choice)
    if choice == 0:
        break

    SystemChoice = random.randint(1,3)
    SystemChoiceString = "" 
    if SystemChoice == 1 : SystemChoiceString = "Rock"
    elif SystemChoice == 2 : SystemChoiceString = "Paper"
    elif SystemChoice == 3 : SystemChoiceString = "Scissors"
    print("System's choice is : " +SystemChoiceString)
    if(SystemChoice == 1 and choice == 2) or (SystemChoice == 2 and choice == 3) or (SystemChoice == 3 and choice == 1):
        print("You won !!!")
        score+=1
    elif SystemChoice == choice :
        print("Tie !!!")
    else :
        print("You lost !!!")
        score-=1
    print("\n\n")

