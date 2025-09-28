import random  # Used to generate random choices for the computer

# Dictionary mapping user inputs to numbers for easier comparison
youdic = {"s": 1, "p": 2, "sc": 3}

# Reverse dictionary to convert numbers back to words for display
reversedic = {1: "stone", 2: "paper", 3: "scissor"}

# Lists of messages for variety in results
Win_messages = [
    "🔥 Boom! You crushed this round!",
    "✨ Victory is yours!",
    "😎 You outsmarted the computer!",
    "🎯 Perfect move!"
] 
lose_messages = [
    "💀 Oops! Computer got you this time.",
    "🤖 AI wins this one!",
    "😢 Better luck in the next round.",
    "⚡ Computer outplayed you!"
]
Draw_messages = [
    "😐 It's a tie!",
    "🤝 Both chose wisely, no winner this time.",
    "🔄 Round ended in a draw.",
    "😅 Great minds think alike!"
]

# Initial scores for both player and computer
your_score = 0
computer_score = 0

# Function to create a visual separator for readability
def Boundary():
    return "_____________________________________________________________________"

# --- Computer Choice Functions ---

# Easy mode: 10% chance computer deliberately loses
def computer_choiceE(you):
    if random.random() < 0.10:
        if you == 1:   # Player chose stone
            return 3   # Computer picks scissor → player wins
        elif you == 2: # Player chose paper
            return 1   # Computer picks stone → player wins
        else:          # Player chose scissor
            return 2   # Computer picks paper → player wins
    else:
        return random.choice([1, 2, 3])  # Normal random choice

# Medium mode: 5% chance computer deliberately loses
def computer_choiceM(you):
    if random.random() < 0.05:
        if you == 1:
            return 3
        elif you == 2:
            return 1
        else:
            return 2
    else:
        return random.choice([1, 2, 3])

# Hard mode: Computer always plays randomly (no deliberate mistakes)
def computer_choiceH(you):
    return random.choice([1, 2, 3])


# Variable to control "play again" functionality
play_again = "y"

# --- Outer Game Loop (runs until player chooses to stop) ---
while play_again == "y":

    # Ask player to select difficulty mode
    m = input("\nEnter mode (e = easy, me = medium, h = hard): ").lower()

    # Reset scores at the start of each new game
    your_score = 0
    computer_score = 0

    # Input validation for game mode
    while m not in ("e", "me", "h"):
        m = input("Please enter a valid mode (e, me, h): ")

    print("\nGame Started! First to reach 10 points wins.\n")

    # --- Main Game Loop (runs until someone reaches 10 points) ---
    while your_score < 10 and computer_score < 10:

        # Get player input and convert to lowercase
        yourstr = input("Enter your choice (s = stone, p = paper, sc = scissor): ").lower()

        # Input validation
        if yourstr not in youdic:
            print("\n⚠️ Invalid input! Please choose: s (stone), p (paper), or sc (scissor).\n",
                  Boundary(), "\n")
            continue  # Skip invalid input and restart loop

        # Convert player input into number form
        you = youdic[yourstr]

        # Computer selects its move based on chosen difficulty mode
        if m == "e":
            computer = computer_choiceE(you)
        elif m == "me":
            computer = computer_choiceM(you)
        else:  # Hard mode
            computer = computer_choiceH(you)

        # Show both player’s and computer’s choices
        print(f"\nYou picked → {reversedic[you]}\nComputer picked → {reversedic[computer]}")

        # --- Determine Round Result ---
        if computer == you:  # Draw
            print("\n", random.choice(Draw_messages), "\n")
        elif (computer == 1 and you == 2) or (computer == 2 and you == 3) or (computer == 3 and you == 1):
            # Player wins
            print("\n", random.choice(Win_messages), "\n")
            your_score += 1
        else:
            # Computer wins
            print("\n", random.choice(lose_messages), "\n")
            computer_score += 1

        # Show current scoreboard
        print(f"Scoreboard → You: {your_score} | Computer: {computer_score}\n")
        print("Let’s go, next round.......!")
        print(Boundary(), "\n")

    # --- End of Game Result ---
    if your_score == 10:
        print("🎉 Congratulations! You won the game!\n\n")
    else:
        print("😢 Computer won the game! Better luck next time.\n\n")

    # Ask if player wants to play again
    play_again = input("Do you want to play again? (y/n): ").lower()

    # Input validation for play again option
    while play_again not in ["y", "n"]:
        play_again = input("Please enter 'y' or 'n': ").lower()

# Exit message after quitting
print("\nThanks for playing! 👋\n\n")

