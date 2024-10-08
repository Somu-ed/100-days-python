## A little bit of math

So far we have introduced the computer to two types of numbers:

- `float`: numbers with a decimal
- `int`: whole numbers

👉 Copy this code and have a go with trying the different mathematical symbols.

```python
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
```


## Let's split the bill

Did you have fun messing with those mathematical symbols? Now let's put them to good use.

You and your friends went to dinner and need to split the bill. Being the clever friend you are, you can use your code to discover how much each person owes. (Remember, `myBill` is a float because the total bill will probably have a decimal point and `numberOfPeople` is an `int` because you did not go to dinner with .7 of a person.)

👉 Copy this code and see what happens:

```python
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
print("You all owe", answer)
```

Did you get a really funky number with sooo many decimal points?

You can take your answer and use `round`. Round has two components: "What am I rounding?" and "How many decimal places am I rounding to?"

Add this portion of code after `answer` and before `print`. This shows you are rounding `answer` to 2 decimal points.

```python
answer = round(answer, 2)
```


## 👉 Day 10 Challenge

### Extend your bill calculator

Add a tip function that adds the total tip to the bill before splitting it equally between the people.

1. Ask the user for the total bill amount.
2. Ask what % of tip they will leave to be added to the bill total.
3. Figure out how to get the total bill with tip then add that to original amount.
4. Ask the user how many people are splitting the bill and divide by the total.

You can use the same code to get started:

```python
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
print("You all owe", answer)
```
