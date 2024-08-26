# operators
adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)

# -------------------------------------------------------------

## Fix my code!

# multiplication
print(3.4 * 6.8)

# division
print(2467 / 4673)

#raise 10 to the power of 2
print(10**2)

# print the remainder when 343 is divided by 4
print(343 % 4)

# --------------------------------------------------------------

## Day 10 Challenge

print("Tip Calculator")
print("---------------")

print()
myBill = float(input("What was the bill?: "))

print()
numberOfPeople = int(input("How many people?: "))

print()
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent? "))

bill_with_tip = tip / 100 * myBill + myBill
bill_per_person = bill_with_tip / numberOfPeople
final_amount = round(bill_per_person, 2)

print()
print("You all owe", final_amount)

