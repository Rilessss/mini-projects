import random

top_of_range = input("enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("enter a number higher than 0!")
        quit()
else:
    print("enter a NUMBER!")
    quit()


r = random.randrange(-1,top_of_range)
guesses = 0
while True:
    guesses +1
    guess = input("guess the number ")
    if guess.isdigit():
       guess = int(guess)

    else:
        print("enter a NUMBER!")
        continue

    if guess == r:
        print("correct")
        break
    else:
        print("wrong")
print("you got it correct after", guesses, "guesses !")