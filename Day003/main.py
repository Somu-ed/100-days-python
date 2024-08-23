# concatenation
myName = input("What's your name? ")
myLunch = input("What are you having for lunch? ")
print(myName, "is going to be chowing down on", myLunch, "very soon!")

# example
number = input("Give me a number: ")
group = input("Give me a collective noun for a group of things: ")
thing = input("Give me the name of a weird or wacky thing: ")
print("No I don't think that", number, "is a", group, "of", thing,". That's just odd.")

# ------------------------------------------------

## Fix my Code!

# print("=== Your Song Generator ===")
# print("""You'll be asked a bunch of questions
# then we'll make you up an amazing
# song, totally copyright free 😭""")
# print()
# person = input("Name a person famous for something good: ")
# thing = input("Name a thing they did: ")
# place = input("Name a place you like: ")
# rhyme = input("Give me a verb that rhymes with your person's name: ")
# print()
# print("There was a person called" name)
# print("Who did something cool like", thing, "at the wonderful", place "where you'll find me", rhyme)

# Answer
print("=== Your Song Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
song, totally copyright free 😭""")
print()

person = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your person's name: ")

print()
print("There was a person called", person, "Who did something cool like", thing, "at the wonderful", place,  "where you'll find me", rhyme)

# ------------------------------------------------

## Day 3 Challenge:

# 1
food = input("Name a type of food: ")
plant = input("Name a plant: ")
cookingType = input("What is a way to cook something? ")
burntFood = input("How do you describe burnt food? ")
householdItem = input("Name something in your house: ")
# 2
print()
print("Tonight's dinner:")

print("For dinner you should make", cookingType, food, "with", burntFood, plant, "on a plate of", householdItem)

# My own version

# Starter
starterFood = input("Name a type of appetizer: ")
starterPlant = input("Name a herb: ")
starterCookingType = input("What's a quick way to cook something? ")
starterHouseholdItem = input("Name a small household item: ")

# Main Course
mainFood = input("Name a main dish: ")
mainPlant = input("Name a vegetable: ")
mainCookingType = input("What's an elaborate way to cook something? ")
mainHouseholdItem = input("Name a large household item: ")

# Dessert
dessertFood = input("Name a sweet treat: ")
dessertPlant = input("Name a fruit: ")
dessertCookingType = input("What's a cold way to prepare food? ")
dessertHouseholdItem = input("Name a fancy household item: ")

print()
print("Tonight's Wacky Three-Course Dinner:")

print("Starter:")
print("For the appetizer, you should make", starterCookingType, starterFood, "with", starterPlant, "served on a", starterHouseholdItem)

print("\nMain Course:")
print("For the main dish, you should prepare", mainCookingType, mainFood, "with", mainPlant, "presented on a", mainHouseholdItem)

print("\nDessert:")
print("For dessert, you should create", dessertCookingType, dessertFood, "with", dessertPlant, "arranged in a", dessertHouseholdItem)