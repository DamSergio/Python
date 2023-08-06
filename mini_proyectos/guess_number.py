import random
import time

def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0

    while guess_number != random_number:
        guess_number = int(input(f"Guess the number between 1 and {x}: "))

        if guess_number < random_number:
            print("Your number is too low")
        elif guess_number > random_number:
            print("Your number is too high")
        else:
            print(f"You guess it! The number was {random_number}")

def computer_guess(x):
    low = 1
    high = x + 1
    guess_number = 0
    random_number = random.randint(low, high)
    print(random_number)

    while guess_number != random_number:
        numbers = list(range(low, high))
        guess_number = numbers[(len(numbers)- 1) // 2]

        if guess_number > random_number:
            high = guess_number
            print(f"{guess_number} is too high")

        elif guess_number < random_number:
            print(f"{guess_number} is too low")
            low = guess_number + 1

        time.sleep(.5)


    print(f"You guess it! The number was {random_number}")

#guess(10)
computer_guess(1000000)