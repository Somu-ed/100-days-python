# Nesting
tvShow = input("What is your favorite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favorite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
  else:
    print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")


# -----------------------------------------------

## Fix my code
# order = input(What would you like to order: pizza or hamburger? ")
# if order = "hamburger":
# print("Thank you.")
#   cheese = input("Do you want cheese?")
#   if cheese == "yes":
#   print("You got it.")
# else:
#     print("No cheese it is.")
# elif order == pizza:
#   print("Pizza coming up.")
#   toppings = input("Do you want pepperoni on that?")
#   if toppings = "yes"
#     print("We will add pepperoni.")
# else:
#   print"Your pizza will not have pepperoni.")

# Answer
order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger":
  print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
    print("You got it.")
  else:
    print("No cheese it is.")
elif order == "pizza":
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes":
    print("We will add pepperoni.")
  else:
    print("Your pizza will not have pepperoni.")

# -----------------------------------------------

## Day 7 Challenge

print("Are you a superfan of 'The Big Bang Theory' or a fake fan?")
print()
print("Answer these questions to find out.")
print("Note: use Lowercase for all answers!!")
print()

Glasses = input("Does someone wear glasses? ")
print()

if Glasses == "yes":
  print("Great Scott! You've got the vision of an eagle!")
  print()

  Catchphrase = input("What's Sheldon's catchphrase? ")
  print()

  if Catchphrase == "bazinga":
    print("Holy protons! You're on fire!")
    print()

    Apartment = input("What's Sheldon and Leonard's apartment number? ")
    print()

    if Apartment == "4a":
      print("Eureka! You're as smart as a Wolowitz... maybe smarter!")
    else:
      print("Oops! Looks like someone needs to binge-watch a few more episodes!")
  else:
    print("Bazinga! You fell for that one!")
else:
  print("Uh-oh! Seems like you need to adjust your TV settings!")
  print()

  WhoGlasses = input("And who wears glasses? ")
  print()

  if WhoGlasses == "leonard":
    print("By Einstein's hair, you've redeemed yourself!")
    print()

    Job = input("What's Penny's job in the early seasons? ")
    print()

    if Job == "waitress":
      print("Holy Cheesecake Factory! You're on a roll!")
      print()

      Where = input("Where does she work? ")
      print()

      if Where == "cheesecake factory":
        print("Great caesium! You're as observant as Sheldon in a comic book store!")
      else:
        print("Close, but no Penny Blossoms!")
    else:
      print("Looks like someone's been hitting the Romulan ale!")
  else:
    print("Good Lord! Even Raj could've answered that after a few drinks!")
    print()

    University = input("Where do the guys work? ")
    print()

    if University == "caltech":
      print("By Spock's ears, you've salvaged some nerd cred!")
    else:
      print("Great barriers! You're more lost than Sheldon without his spot!")

print()
print("Thanks for playing! May the Force be with... oops, wrong franchise!")