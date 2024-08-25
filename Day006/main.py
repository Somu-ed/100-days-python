# elif statement
print("SECURE LOGIN")
username = input("Username > ")

if username == "mark":
  print("Welcome Mark!")
elif username == "suzanne":
  print("Hey there Suzanne!")
else:
  print("Go away!")

# example 2
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password > ")

if username == "mark" and password == "password":
  print("Welcome Mark!")
elif username == "suzanne" and password == "Su74nne":
  print("Hey there Suzanne!")
else:
  print("Go away!")


# -------------------------------------------------------

## Fix my code

# season = input(what is your favorite season?)
# if season = "spring"
#   print("Ah! The birds are chirping and flowers blooming.")
#   elif season == summer:
#   print("Catch some sun and cool off with a lemonade.")
# elif season == autumn
# print("The leaves are changing and the air is crisp. Enjoy!)
#       elif season = winter:
#       print("Stay warm by the fire and watch the snow fall.")
# else:
# print("I don't know that season. Please try again.")


# Answer:
season = input("What is your favorite season?")
if season == "spring":
  print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
  print("Catch some sun and cool off with a lemonade.")
elif season == "autumn":
  print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
  print("Stay warm by the fire and watch the snow fall.")
else:
  print("I don't know that season. Please try again.")


# -------------------------------------------------------

## Day 6 Challenge

print("Secure Login")

# Collect username and password from the user
username = input("What is your username? ")
password = input("What is your password? ")

# Check credentials and respond accordingly
if username == "David" and password == "PyTh0nR*cks":
  print("Welcome, David! You are looking nice today!")
elif username == "Becky" and password == "Repl!t4evEr":
  print("Hi Becky! Love your hair today!")
elif username == "Bill" and password == "SmashTHEb*gs!":
  print("Yo! Bill! What up?!")
else:
  print("You do not have access. Go away!")

