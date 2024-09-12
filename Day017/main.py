# continue & exit() in while loop
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")

# -------------------------------------------------------------

## Fix my code!
# print("Let's play chutes and ladders. Pick ladder or chute.")
# while True:
#   print("Do you want to go up the ladder or down the chute?")
#   direction = input("> ")
#   if direction == "chute"
#     print("Game over!")
#   break
#   elif direction == "ladder":
#     continue
# else:
#     print("Game over!")
#     exit 
# print("Thanks for playing!")

print("Let's play chutes and ladders. Pick ladder or chute.")
while True:
  print("Do you want to go up the ladder or down the chute?")
  direction = input("> ")
  if direction == "chute":
    print("Game over!")
    break
  elif direction == "ladder":
    continue
  else:
    print("Game over!")
    exit ()
print("Thanks for playing!")

# -------------------------------------------------------------

# Day 17 Challenge

from getpass import getpass as input

player1_score = 0
player2_score = 0

while True:
    print("\nE P I C    🪨  📄 ✂️    B A T T L E ")
    print(f"\nScore - Player 1: {player1_score}, Player 2: {player2_score}")
    print("\nSelect your move (R, P or S)")
    print()

    player1Move = input("Player 1 > ").upper()
    print()
    player2Move = input("Player 2 > ").upper()
    print()

    if player1Move not in ["R", "P", "S"]:
        print("🚫 Oops! Player 1, please choose R, P, or S only!")
        continue

    if player2Move not in ["R", "P", "S"]:
        print("🚫 Oops! Player 2, please choose R, P, or S only!")
        continue

    if player1Move == player2Move:
        print("🤜🤛 It's a draw! Great minds think alike!")
    elif player1Move == "R":
        if player2Move == "S":
            print("💥 Player 1's Rock crushes Player 2's Scissors! Player 1 wins!")
            player1_score += 1
        else:
            print("🌟 Player 2's Paper wraps Player 1's Rock! Player 2 wins!")
            player2_score += 1
    elif player1Move == "P":
        if player2Move == "R":
            print("📜 Player 1's Paper covers Player 2's Rock! Player 1 wins!")
            player1_score += 1
        else:
            print("✂️ Player 2's Scissors cut through Player 1's Paper! Player 2 wins!")
            player2_score += 1
    else:  # player1Move == "S"
        if player2Move == "P":
            print("✂️ Player 1's Scissors shred Player 2's Paper! Player 1 wins!")
            player1_score += 1
        else:
            print("💪 Player 2's Rock smashes Player 1's Scissors! Player 2 wins!")
            player2_score += 1

    if player1_score == 3:
        print("\n🎉 Player 1 wins the game!")
        break
    elif player2_score == 3:
        print("\n🎉 Player 2 wins the game!")
        break

print(f"\nFinal Score - Player 1: {player1_score}, Player 2: {player2_score}")