# type casting int

myScore = int(input("Your score: "))
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")


# type casting float

myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")


# ------------------------------------------------

## Fix my code
# score = input("What was your score on the test?"))
# if score >= 80
#   print("Not too shabby")
# elif score > "70":
#   print("Acceptable.")
# else:
# print("Dude, you need to study more!")

# Answer
score = int(input("What was your score on the test?"))
if score >= 80:
  print("Not too shabby")
elif score >= 70:
  print("Acceptable.")
else:
  print("Dude, you need to study more!")

# ------------------------------------------------

## Day 9 Challenge


birthYear = int(input("What year were you born? "))
if birthYear <= 1946:
  print("You are a Traditionalist.")
elif birthYear >= 1947 and birthYear <= 1964:
  print("Hey, Baby Boomer! How you doing?")
elif birthYear >= 1965 and birthYear <= 1981:
  print("Gen X! What's up?")
elif birthYear >= 1982 and birthYear <= 1995:
  print("Millenials! The age of tech!")
elif birthYear >= 1996:
  print("Hey, Gen Z! TikTok much?")
else:
  print("Try again!")