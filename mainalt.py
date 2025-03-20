'''
0 for stone
1 for paper
-1 for  scissors

CUTTTTTT!!!!!
'''
import random

while True:
    computer= random.choice([-1, 0, 1])


    youstr =input("Enter your choice amoung p,sc,st:\n  ")
    
    if youstr.lower()== 'ex':
        print("Exiting game, Goodbye. \nThanks for playing.")
        break
    
    youDict= {"p" : 1, "sc": -1, "st": 0}
    reverseDict= {1 : "paper", -1 : "scissors", 0 : "stone"}
    
    if youstr not in youDict:
        print("Please enter a valid input.")
    
    you = youDict[youstr]

    print(f" You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

    if(computer == you):
        print("It's a Draw!")

    else:
        if(computer == -1 and you == 1):
            print("You Lose!")
        
        elif(computer == -1 and you == 0):
            print("You Win!")
            
        elif(computer == 1 and you == -1):
            print("You Win!")
            
        elif(computer == 0 and you == -1):
            print("You Lose!")
            
        elif(computer == 0 and you == 1):
            print("You Win!")
            
        elif(computer == 1 and you == 0):
            print("You Lose!")

        else:
            print("Something went wrong!")