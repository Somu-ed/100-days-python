# while loop
counter = 0
while counter < 10:
  print(counter)
  counter +=1


# -------------------------------------------------------------

## Fix my code!

# counter = 0
# while counter < 25:
#   print(counter)

counter = 0
while counter < 25:
  print(counter)
  counter +=1

# counter = 0
# while counter >= 12:
#   print(counter)
#   counter += 1

counter = 0
while counter <= 12:
  print(counter)
  counter += 1

# exit = ""
# while exit = "yes":
#   print("🥳")
# exit = input("Exit?: ")

exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")


# -------------------------------------------------------------

## Day 15 Challenge


exit = "no"


while exit == "no":
  animal_sound = input("What animal sound do you want to hear?: ")
  print()

  if animal_sound == "cow" or animal_sound == "Cow":
    print("🐮 Moo")
  elif animal_sound == "pig" or animal_sound == "Pig":
    print ("🐷 Oink")
  elif animal_sound == "sheep" or animal_sound == "Sheep":
    print ("🐑 Baaa")
  elif animal_sound == "duck" or animal_sound == "Duck":
    print("🦆 Quack")
  elif animal_sound == "dog" or animal_sound == "Dog":
    print("🐶 Woof")
  elif animal_sound == "cat" or animal_sound == "Cat":
    print("🐱 Meow")
  else:
    print("I don't know that animal sound. Try again.")

  print()
  exit = input("Do you want to exit?: ")
  print()