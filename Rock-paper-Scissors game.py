import random

choices = ["Rock", "Paper", "Scissors"]
cpu_score = 0
player_score = 0
last_computer_choice = None  # Track previous computer move

print("🎮 Welcome to Rock, Paper, Scissors!")
print("Type 'End' anytime to quit.\n")

while True:
    player = input("Rock, Paper or Scissors? ").capitalize()

    if player == "End":
        print("\n🧾 Final Scores:")
        print(f"CPU: {cpu_score}")
        print(f"Player: {player_score}")
        print("👋 Thanks for playing!")
        break

    if player not in choices:
        print("❌ Invalid input. Please enter Rock, Paper, or Scissors.")
        continue

    # Exclude last computer choice
    available_choices = [c for c in choices if c != last_computer_choice]
    computer = random.choice(available_choices)
    last_computer_choice = computer  # Update history

    print(f"🤖 Computer chose: {computer}")

    if player == computer:
        print("🤝 It's a tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("📄 You lose! Paper covers Rock.")
            cpu_score += 1
        else:
            print("🪨 You win! Rock smashes Scissors.")
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("✂️ You lose! Scissors cut Paper.")
            cpu_score += 1
        else:
            print("📄 You win! Paper covers Rock.")
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("🪨 You lose! Rock smashes Scissors.")
            cpu_score += 1
        else:
            print("✂️ You win! Scissors cut Paper.")
            player_score += 1