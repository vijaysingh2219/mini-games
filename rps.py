from random import randrange
import json


def rps():
    choices = ["rock", "paper", "scissors"]
    userChoice = input("Choose :[rock, paper, scissors]: ")
    botChoice = choices[randrange(len(choices))]
    result = ''
    if (userChoice == 'rock' and botChoice == "scissors") or (userChoice == "paper" and botChoice == "rock") or (userChoice == "scissors" and botChoice == "paper"):
        result = "You Won"
        print(
            f"Bot Choose: {botChoice}\nUser Choice: {userChoice}\nResult: {result}")

    elif (userChoice == botChoice):
        result = "Tie"
        print(
            f"Bot Choose: {botChoice}\nUser Choice: {userChoice}\nResult: {result}")

    else:
        result = "You Lose"
        print(
            f"Bot Choose: {botChoice}\nUser Choice: {userChoice}\nResult: {result}")
