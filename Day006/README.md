## What the elif is this?

- The `elif` command (which stands for 'elseif') allows you to ask 2, 3, 4 or 142 questions using the same input! This command must be in a certain place. You can have as many `elif` statements as you want, but they **must** go in between `if` and `else` and have the same indentation. The `print` statements in your `elif` command need to line up with the indent of the other `print` statements.

Where would an `elif` statement go in the code below?

```python
print("SECURE LOGIN")
username = input("Username > ")
if username == "mark":
  print("Welcome Mark!")
else:
  print("Go away!")
```

👉 Add this `elif` statement to the code above. Make sure you indent properly AND put it in **between** the `if` and `else` statements!

```python
elif username == "suzanne":
  print("Hey there Suzanne!")
```

Your code should look like this:

```python
print("SECURE LOGIN")
username = input("Username > ")

if username == "mark":
  print("Welcome Mark!")
elif username == "suzanne":
  print("Hey there Suzanne!")
else:
  print("Go away!")
```


## Add a password

### Let's add a bit more input.

👉 Now that we have input for both a username and password, we need to change our `if` and `elif` statements just a bit so both the username and password must match for Mark and Suzanne to login.

```python
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")
```

👉 In the code below the username and password must **both** be correct for Mark to login.

```python
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")
if username == "mark" and password == "password":
 print("Welcome Mark!")
elif username == "suzanne":
 print("Hey there Suzanne!")
else:
 print("Go away!")
```

👉 Suzanne's password is 'Su74nne'. Can you add that to the code above? (HINT: It should be very similar to Mark.)

```python
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "mark" and password == "password":
 print("Welcome Mark!")
elif username == "suzanne" and password == "Su74nne":
 print("Hey there Suzanne!")
else:
 print("Go away!")
```


## Common Errors

First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

### Syntax Error

👉 What is wrong the code below?

```python
print("SECURE LOGIN")
username = input("Username > ")
if username == "mark":
  print("Welcome Mark!")
else:
  print("Go away!")
elif username == "suzanne":
  print("Hey there Suzanne!")
```

The `elif` statement is in the wrong place. It must go in between the if and else statements.

```python
print("SECURE LOGIN")
username = input("Username > ")
if username == "mark":
  print("Welcome Mark!")
elif username == "suzanne":
  print("Hey there Suzanne!")
else:
  print("Go away!")
```


## 👉 Day 6 Challenge

### Make your own login program.

1. Create a program where someone logins with their username and password correctly and then gets a lovely individual greeting.
2. Write a specific personalized greeting for 3 different people.
3. Don't forget an `else` statement for everyone else who shouldn't be logging in.

