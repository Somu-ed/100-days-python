# if..else statement
myName = input("What's your name?: ")
if myName == "David":
  print("Welcome Dude!")
  print("You're just the baldest dude I've ever seen")
else:
  print("Who on earth are you?!")

# -----------------------------------------------------------

## Fix my Code!
# drink = input("Do you prefer coffee or tea?)
# if drink = "coffee"
#   print("Tea is better.")
#     else:
#   print("Excellent choice.")

# Answer
drink = input("Do you prefer coffee or tea?")
if drink == "coffee":
  print("Tea is better.")
else:
  print("Excellent choice.")

# -----------------------------------------------------------

## Day 5 Challenge

print("Which character are you from 'Avengers?'")
print()
print("Answer these questions and let's find out.")
print()
print("Please use Y or N for yes and no.")

likeGreen = input("Do you like the color green?: ")
if likeGreen == "Y":
  print("You must be the Hulk!")

IronIsCool = input("Do you think building robots is cool?: ")
if IronIsCool == "Y":
  print("You must be Iron Man. Cool suit!")

TimeTravel = input("Do you like traveling through time?: ")
if TimeTravel == "Y":
  print("You must be Captain America!")

Strong = input("Are you super strong?: ")
if Strong == "Y":
  print("You have got to be Thor!")

if likeGreen == "Y" or IronIsCool == "Y" or TimeTravel == "Y" or Strong == "Y":
  print("Welcome to the 'Avengers' !!")
else:
  print("I guess you are not like anyone from 'Avengers.'")