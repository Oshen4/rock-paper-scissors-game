import random

choices = ["Rock", "Paper", "Scissors"]

while True:
    user_choice = input("Enter: Rock, Paper, or Scissors (or use 'quit' to stop): ").lower()

    if user_choice == 'quit':
        print("Thanks for Playing!")
        break

    if user_choice not in choices:
        print("Not a valid choice")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors" ) or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        print("You Win!")
    else:
        print("You Lose!")

    print()