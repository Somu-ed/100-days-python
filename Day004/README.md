## Sneaky Extra Skill

You can jazz things up even more by changing the color of the text. Wow. We're quickly approaching the quality of output of a computer from 1981! 😬

### How does it work?

- It's all just `print` statements, but using special codes that tell your console to start ***printing everything after this point*** in the new color.
- You will need to reset if you want to go back and change it in previous lessons.

![print in color](image.png)

The somewhat random characters in the print argument are telling the computer to change the color of the next text output to whichever color you pick.
You must add the number from the table below.

| Color | Value |
| --- | --- |
| Default | 0 |
| Black | 30 |
| Red | 31 |
| Green | 32 |
| Yellow | 33 |
| Blue | 34 |
| Purple | 35 |
| Cyan | 36 |
| White | 37 |

### Example

Something like this would allow you to have a red `warning` in the middle of the output.

```python
print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")
```


## 👉 Day 4 Challenge

Everyone loves a good story!

Well, you're going to create your own adventure story that places your user in the role of the main character and we'll even customize the story to suit their interests.

### Your task

1. Ask your users to list a bunch of information about them: things they like, things they hate, names of family and friends... it's up to you how many and what kinds of things you pick. Keep it wacky!

2. Now construct your story - it can be about anything you want, but must use the variables you've created in step 1.

3. Make sure to only work one paragraph at a time. Otherwise things could get a ***bit messy***.

### Example

Everything which is within the curly braces `{...}` is what you need to ask the user, store it in a variable and then display that in your story.

```
Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!

What is your name?
What is your worst enemy’s name?
What is your superpower?
Where do you live?
What is your favorite food?

Hello {name}! Your ability to {superpower} will make sure you never have to look at {worst enemy’s name} again. Go eat {your favorite food} as you walk down the streets of {where you live} and use {superpower} for good and not evil!
```