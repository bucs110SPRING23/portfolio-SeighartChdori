import random

ran = random.randint(1,10)

for x in range(3):
    guess = input("Can you guess the random number?\nChoose a number from 1 to 10 : ")

    if int(guess) > ran :
        print("Too High")    
    elif int(guess) < ran :
        print ("Too Low")
    else :
        print ("Correct!")

    if x == 2 and int(guess) != ran :
        print ("Unforunately, the correct answer is", ran)