import random
import sys
import time

def choice1():
    print("This is your story. Choose this thing (1) or other thing (2)")
    choice = input()
    while choice != "1" and choice != "2":
        choice = input("Choose 1 or 2: ")
    if choice == "1":
        print("Do a thing.")
    else:
        print("Do another thing")
    return choice

def choice2(firstChoice):
    print("More story stuffs")
    if firstChoice == "1":
        print("Do a thing")
        choice = input("Present a choice (1) or (2) ")
        while choice != "1" and choice != "2":
            choice = input("Choose 1 or 2: ")
        if choice == "1":
            print("Do a thing.")
        else:
            print("Do another thing")
    else:
        print("Do a slightly different thing")
        choice = input("Present a choice (1) or (2) ")
        while choice != "1" and choice != "2":
            choice = input("Choose 1 or 2: ")
        if choice == "1":
            print("Do a thing.")
            choice = "3"
        else:
            print("Do another thing")
            choice = "4"
    return choice


firstChoice = choice1()
choice2(firstChoice)
