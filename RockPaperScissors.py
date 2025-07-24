import random

CHOICES = {1: "Rock", 2: "Paper", 3: "Scissors"}

WINNING_COMBOS = {
    ("Rock", "Scissors"): "Rock",
    ("Scissors", "Paper"): "Scissors",
    ("Paper", "Rock"): "Paper"
}

def get_user_choice():
    print("\nChoose your move:\n 1. Rock\n 2. Paper\n 3. Scissors")
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice in CHOICES:
                return CHOICES[choice]
            print("Please choose a valid option (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return CHOICES[random.randint(1, 3)]

def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    winner = WINNING_COMBOS.get((user, computer)) or WINNING_COMBOS.get((computer, user))
    return "User" if winner == user else "Computer"

def play_round():
    user_move = get_user_choice()
    comp_move = get_computer_choice()

    print(f"\nYou chose: {user_move}")
    print(f"Computer chose: {comp_move}")
    print(f"{user_move} vs {comp_move}")

    outcome = determine_winner(user_move, comp_move)

    if outcome == "Tie":
        print("<== It's a tie! ==>")
    elif outcome == "User":
        print("<== You win! ==>")
    else:
        print("<== Computer wins! ==>")

def play_game():
    print("Welcome to the Rock, Paper, Scissors game!")
    print("Rock vs Paper -> Paper wins")
    print("Paper vs Scissors -> Scissors wins")
    print("Rock vs Scissors -> Rock wins")

    while True:
        play_round()
        again = input("\nDo you want to play again? (Y/N): ").strip().lower()
        if again != 'y':
            break

    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    play_game()
