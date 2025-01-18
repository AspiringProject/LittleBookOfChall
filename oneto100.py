import random
def generate():
    num = random.randint(1,100)
    return num

def guessing():
    attempts = 0
    num = generate()
    guess = int(input("Guess a number between 1 and 100: "))
    while guess != num:
        if guess < num:
            print("Higher")
            attempts = attempts + 1
        else:
            print("Lower")
            attempts = attempts + 1
        guess = int(input("Guess again: "))
    print("You got it!")
    print("It took you", attempts, "attempts")

guessing()