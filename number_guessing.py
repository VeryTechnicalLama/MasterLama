print("Welcome to number guessing game!")
player1 = input("Please enter your name")
print(f"Hello {player1}!")
player2 = input("Please enter your neme")
print(f"Hello {player2}")

numtoguess = int(input(f"{player1} please enter number from 1 - 100"))
numchosen = int(input(f"{player2} now try to guess number of {player1}"))

if numtoguess == numchosen:
    print("Whell done! You've guessed the number")
else:
    print("Try again")
