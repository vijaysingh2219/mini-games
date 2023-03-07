from diceroll import diceroll
from rps import rps
from highlow import highlow

if __name__ == "__main__":
    print("Enter the type of game you want to play:\n(1) highlow\n(2) rps\n(3) diceroll")
    ans = int(input("Enter Serial No. : "))

    if ans == 1:
        result = highlow()
    elif ans == 2:
        result = rps()
    elif ans == 3:
        result = diceroll()
    else:
        print("Invalid Input, Try again!")
