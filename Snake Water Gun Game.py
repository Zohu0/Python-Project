# Snake Gun Water

import random

def game(comp, you):
    
        if comp=="snake" and you=="gun":
            return ("You Win")
        elif comp=="gun" and you=="snake":
            return ("Computer Win")
        elif comp=="snake" and you=="water":
            return ("Computer Win")
        elif comp=="water" and you== "gun":
            return ("Computer Win")
        elif comp=="gun" and you=="water":
            return ("You Win")
        elif comp=="water" and you=="snake":
            return ("You Win")
        else:
            return ("The Game Is Tie")

print("Computer Turn: 'snake' 'water' or 'gun'")
randNo= random.randint(1,3)
if randNo==1:
    comp= "snake"
elif randNo==1:
    comp="gun"
elif randNo== 3:
    comp="water"

you=input("Your Turn: 'snake' 'water' or 'gun': ")

games=game(comp, you)

print("Computer Choose: " + comp)
print("You Choose: " + you)
print(games)
 
