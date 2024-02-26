import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess the number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, To Low")
        elif guess > random_number:
            print("Sorry, To High")
                    

    print(f'Congrats you have the guessed the correct number {random_number}')

guess(50)

