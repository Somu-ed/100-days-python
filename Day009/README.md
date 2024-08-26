## Casting

`If` statements support more than `==`. They support inequality symbols as well. Remember those <, >, and = signs you used in math way back when? Well they are back again, but this time they look a bit different.

Equality and Inequality Symbols

```python
# equal
5 == 5

# not equal
3 != 5

# greater than
5 > 3

# greater than or equal to
5 >= 3

# less than
3 < 5

# less than or equal to
3 <= 5
```

This is because the way `input` works behind the scenes is it always assumes what you are typing is text (or a string) and gets stored as a variable in `""`.

*Casting* is where we explicitly tell the computer that what we are typing is a number and not a letter.

The code below is saying any score greater than 100,000 is a winner. Anything less, try again.

👉`Run` this code in `main.py` and see what happens:

```python
myScore = input("Your score: ")
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
```
We crashed it! How do we tell the computer, "Wait, thats a number!"?


## Let's add `int`

- There are two types of numbers the computer will recognize:
  - int whole number (ex: 42)
  - float any number with a decimal (ex: 1.81)

### int
To change "your score" to a number, we need to add `int` in front of the `input` and place the enitre input in `()`.

```python
myScore = input("Your score: ")
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
```

👉 Update your code to look like this:

```python
myScore = int(input("Your score: "))
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
```

Did it work this time?

The way the computer will read this code is by starting with what is in brackets first ("your score"). The computer thinks this is text because of the `""`. When we add `int`, we are telling the computer, "This is not text. Please convert this to a whole number." Now the variable, `myScore` will store the answer as a number.


## Let's add `float`

You would do the exact same thing, except using `float` for a decimal number. In the code below, I want to find pi to 3 decimal places.

👉 Copy this code and see if it works!

```python
myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")
```

You did it!

We are casting that input as a `float` which means we are expecting a decimal number. The code will not crash if we put a . and then numbers after it to signify a decimal number.


## Common Errors

First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

### Invalid Syntax

👉 What is the error?

```python
myPi = float(input("What is Pi to 3dp? ")
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")
```

We forgot the second closing `)` at the end of our input. Remember, on each line for every open bracket, there needs to be a closing bracket.

### Extra challenge

👉 What is the error?

```python
myPi = float input("What is Pi to 3dp?")
if myPi == 3.142 :
  print("Exactly!)
else:
  print("Try again 😭")
```

We forgot the first opening `(` before `input`. Remember, for casting to float or int, we need to enclose the thing to be casted into starting and closing brackets..

We also forgot to end the double quote ` after `"Exactly!`


## 👉 Day 9 Challenge

### Generation Generator

What generation are you a part of?

Use this list to guide you.

Generation Name | Starting Birth Year | Ending Birth Year
--- | --- | ---
Traditionalists | 1925 | 1946
Baby Boomers | 1947 | 1964
Generation X | 1965 | 1981
Millenials | 1982 | 1995
Generation Z | 1996 | 2015

1. Have a user type in the year they were born.
2. Use their answer to tell them the generation they are a part of.
3. Add emojis or a fun statement to go along with the answers if you like.

