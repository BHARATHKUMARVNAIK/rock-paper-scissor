
import random

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

def play_game():
    print("🪨📄✂️ Welcome to Rock, Paper, Scissors!")
    rounds = 3
    player_score = 0
    computer_score = 0

    options = ["rock", "paper", "scissors"]

    for round in range(1, rounds + 1):
        print(f"\nRound {round}")
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice not in options:
            print("Invalid choice! Please choose again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        result = get_winner(player_choice, computer_choice)

        if result == "player":
            print("✅ You win this round!")
            player_score += 1
        elif result == "computer":
            print("❌ You lose this round.")
            computer_score += 1
        else:
            print("🤝 It's a draw.")

        print(f"Score -> You: {player_score} | Computer: {computer_score}")

    print("\n🎯 Final Result:")
    if player_score > computer_score:
        print("🏆 You win the game!")
    elif player_score < computer_score:
        print("😢 You lost the game.")
    else:
        print("⚖️ It's a tie!")

# Main loop
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing Rock, Paper, Scissors!")
        break
