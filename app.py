import random
import sys

def rock_paper_scissors():
    # Display game options
    print("Lets play rock, paper, scissors!")
    print("1.) Rock")
    print("2.) Paper")
    print("3.) Scissors")
    print("4.) Quit")

    try:
        # Get user's choice
        choice = input("Select a choice: ")

        # Check if the user wants to quit
        if choice == "4":
            print("Exiting\n")
            sys.exit()
        # Check if the user's choice is valid
        elif choice in ("1", "2", "3"):
            # Convert numeric choice to string representation
            choice = {"1": "Rock", "2": "Paper", "3": "Scissors"}[choice]
            print(f"\nYou: {choice}")
        else:
            # Handle invalid choice
            print("Invalid choice")

        # Determine winner based on user and CPU choices
        find_winner(choice, randomize_cpu_choice())
    except (ValueError, KeyboardInterrupt):
        # Handle exceptions for invalid input or user quitting
        print("\nExiting\n")
        sys.exit()
    except Exception as e:
        # Handle other unexpected exceptions
        print(f"An error occurred: {e}\n")

def randomize_cpu_choice():
    # Randomly select CPU's choice
    cpu_options = ["Rock", "Paper", "Scissors"]
    random_index = random.randint(0, len(cpu_options) - 1)
    cpu_choice = cpu_options[random_index]
    print(f"CPU: {cpu_choice}")
    return cpu_choice

def find_winner(player_choice, cpu_choice):
    # Define outcomes based on choices
    outcomes = {"Rock": {"Rock": "Tie", "Paper": "Lose", "Scissors": "Win"},
                "Paper": {"Rock": "Win", "Paper": "Tie", "Scissors": "Lose"},
                "Scissors": {"Rock": "Lose", "Paper": "Win", "Scissors": "Tie"}}

    # Determine and print the winner
    result = outcomes[player_choice][cpu_choice]
    print(f"You {result}!\n")

if __name__ == "__main__":
    # Main game loop
    while True:
        rock_paper_scissors()
