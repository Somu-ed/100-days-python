# DAY 001

## Our first statement

### Print Statements

You just learned your first command: the `print` statement. It says "Print out whatever's in my brackets". The `print` statement is how you get your program to put messages in the console.

![`print`](image.png)

- The `""` (quotes) are used to tell the command that you're putting text in there (any text you want)
- A bunch of text (or whatever you put in quotes) is called a string.

### Multiple Print Statements
👉 Here is what muliple `print` statements looks like. Copy this code into `main.py` and hit `run`.

```python
print("Well we")
print("just use more lines")
print("of code")
```

👉 Use the triple quote `"""` if you want to write a big chunk of text with gaps or line breaks. Add this code to what you have in `main.py` and hit `run`.

```python
print("""Anything that starts
with three quotes, and ends
in three quotes can span
many lines and even contain " symbols
within it without freaking anything out!""")
```

## Common Errors

First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free.

Sometimes you get errors when coding. Here are the most popular errors:

### NameError
- You'll see this error message if:
  - you get the name of a function wrong
  - you misspell it
  - get the capitalization wrong


👉 Let's try to run this code and see what error message we get. Add this code to your coding editor and hit `run`.
```python
Print("What could go wrong?")
```

What do you think is wrong? It's always important to read the error messages as they try to be helpful.

```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    Print("What could go wrong?")
NameError: name 'Print' is not defined
```

Did you notice the p in `print` is capitalized? `print` is only lower case letters.

### SyntaxError
- You will see this message if:
  - you have the order of the symbols wrong
  - you forget () or " "


👉 We will get an error when we run this code. Copy this code to your coding editor and hit `run`.

```python
print "Hello Again"
```

What do you think is wrong?

```
  File "main.py", line 1
    print "Hello Again"
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello Again")?
```

That's right. You forgot `()`.


👉 What is causing the error here? Copy the code and hit run to find out.

```python
print(Please work)
```

```
  File "main.py", line 1
    print(Please work)
                 ^
SyntaxError: invalid syntax
```

You need `" "`.


## Challenge for Day 1
### Project 1: Print into the World
Let's get started with your first project! After only one day, you already have something you can share with the world.

1. Write your `full name` and `today's date` in separate lines of code.

2. Copy this text below. See if you can do it with just the one `print` statement!

```
I am signing up for Replit's 100 days of Python challenge!
I will make sure to spend some time every day coding along, for a minimum of 10 minutes a day.
I'll be using Replit, an amazing online IDE so I can do this from my phone wherever I happend to be. No excuses for not coding from the middle of a field!
```

3. On the next line add `I am feeling` with an emoji of your choice to illustrate how you're feeling about the challenge.

4. Add one more line to your output `You can follow my progress at replit.com/@` and add in your Replit username. This will be a great way of maintaining accountability for yourself!

5. Run your program.