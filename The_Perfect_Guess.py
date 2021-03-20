import random
randnum=random.randint(1, 100)

guesses=0
userguess= None

while (userguess!=randnum):
    userguess=int(input("Guess The Number Between 1 And 100: "))
    guesses=guesses+1
    if (userguess>randnum):
        print("You Guessed It Wrong! Please Guess Lesser Number")
    elif(userguess<randnum):
        print("You Guessed It Wrong! Please Guess Greater Number")
    else:
        print("Congratulation You Guessed It Write")

print(f"You Guessed The Number In {guesses} Time")
