from random import randint


def highlow():
    number = randint(1, 99)
    count = 1

    while True:
        guess_number = int(input("Guess the number: "))
        if (guess_number > number):
            print("You guessed it too high, guess something low.")
            count += 1
        elif (guess_number < number):
            print("You guessed it too low, guess something high.")
            count += 1
        else:
            print(f"You guessed it correct in {count} times")
            return False
