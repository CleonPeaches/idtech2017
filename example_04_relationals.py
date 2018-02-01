#Relational operators and comparison keywords
import random

player_has_item = False
score = 50
won = False

if player_has_item and score > 100:
    won = True

if not won:
    print("You haven't beaten the game yet.")
elif won:
    print("You won the game!")

computer_number = random.randrange(0, 101)
print(computer_number)

guessed = False

while True:
    if guessed:
        answer = input("Guess the number ")
        if int(answer) == computer_number:
            guessed = True
            print("You got it!")
            break
        elif int(answer) > computer_number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

    else:
        break