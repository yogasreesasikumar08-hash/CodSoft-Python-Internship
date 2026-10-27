import random

user_score = 0
computer_score = 0

while True:
    user = input("\nChoose Rock, Paper, or Scissors: ").lower()

    if user not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        continue

    computer = random.choice(["rock", "paper", "scissors"])

    print("Your choice:", user)
    print("Computer's choice:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1

    else:
        print("You Lose!")
        computer_score += 1

    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        print("Thanks for playing!")
        break
