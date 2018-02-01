import random
import time
import sys

player_health = 10


def display_intro():
    print("It is the end of a long and bloody battle.")
    time.sleep(2)
    print("You come to a crossroads on the way back to your village.")
    time.sleep(2)
    print("One path leads home...")
    time.sleep(2)
    print("     ...and the other is known for bandit ambushes.")
    time.sleep(2)


def choose_path():
    path = ""
    while path != str.lower("left") and path != str.lower("right"): # Input validation
        path = input("Which way is home? Left or right?")

    return path


def check_path(chosen_path):
    print("You head down the path")
    time.sleep(2)
    print("You see the hollowed oak you used to play on with the other village children...")
    time.sleep(2)
    print("But your skin begins to crawl...")
    time.sleep(3)

    correct_path = ["left", "right"]
    correct_path = correct_path[(random.randint(1,2))]

    if correct_path == chosen_path:
        print("The feeling passes. You must just be weary from the long battle.")
    else:
        print("An arrow whizzes by and grazes your cheek! You're under attack! ")
        run_or_fight = input("What will you do? Run or fight? ")


play_again = "yes"
while play_again == str.lower("yes"):
    display_intro()
    choice = choose_path()
    check_path(choice)
    play_again = input("Do you want to play again? Type yes or no: ")
    if play_again == str.lower("no"):
        sys.exit()
