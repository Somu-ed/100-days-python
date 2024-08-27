from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()

player1Move = input("Player 1 > ").upper()
print()
player2Move = input("Player 2 > ").upper()
print()

if player1Move == "R" or player1Move == "P" or player1Move == "S":
  if player2Move == "R" or player2Move == "P" or player2Move == "S":
    if player1Move == player2Move:
      print("🤜🤛 It's a draw! Great minds think alike!")
    elif player1Move == "R":
      if player2Move == "S":
        print("💥 Player 1's Rock crushes Player 2's Scissors! Player 1 wins!")
      else:
        print("🌟 Player 2's Paper wraps Player 1's Rock! Player 2 wins!")
    elif player1Move == "P":
      if player2Move == "R":
        print("📜 Player 1's Paper covers Player 2's Rock! Player 1 wins!")
      else:
        print("✂️ Player 2's Scissors cut through Player 1's Paper! Player 2 wins!")
    else:
      if player2Move == "P":
        print("✂️ Player 1's Scissors shred Player 2's Paper! Player 1 wins!")
      else:
        print("💪 Player 2's Rock smashes Player 1's Scissors! Player 2 wins!")
  else:
    print("🚫 Oops! Player 2, please choose R, P, or S only!")
else:
  print("🚫 Oops! Player 1, please choose R, P, or S only!")