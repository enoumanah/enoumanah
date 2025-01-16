import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("enter your choice (rock, paper, scissors)")
    computer_choice = random.choice(choices)

    print("\ncomputer chose {computer_choice}")

    if user_choice == computer_choice:
        print("it is a draw")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("you lose")
        elif computer_choice == "scissors":
            print("you win")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("you lose")
        elif computer_choice == "rock":
            print("you win")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("you lose")
        elif computer_choice == "paper":
            print("you win")