# Day 8 challenge
print("Welcome to your daily affirmation generator!")

print()
name = input("What is your name? ").lower()
day = input("What day of the week is it? ").lower()
color = input("What's your favorite color? ").lower()
animal = input("What's your favorite animal? ").lower()
hobby = input("What's your favorite hobby? ").lower()

print()
if name == "mark":
    if day == "monday":
        print("Hey", name.capitalize() , "! Your love for", color, "things will brighten this Monday!")
    elif day == "tuesday":
        print("Tuesday's looking good,", name.capitalize() , "! Your", animal, "spirit will guide you.")
    elif day == "wednesday":
        print("Happy Hump Day,", name.capitalize() , "! Your", hobby, "skills are improving every day.")
    elif day == "thursday":
        print(name.capitalize() , ", you're almost there! Your perseverance is as strong as a", animal , ".")
    elif day == "friday":
        print("TGIF,", name.capitalize() , "! Time to celebrate with some", hobby , "!")
    else:
        print("Have a great", day.capitalize() , ",", name.capitalize() , "! You're as awesome as a", color, animal , "!")

elif name == "david":
    if day == "monday":
        print("Monday's here,", name.capitalize() , "! Your", hobby, "skills will make this week amazing.")
    elif day == "tuesday":
        print(name.capitalize() , ", your", color, "aura is shining bright this Tuesday!")
    elif day == "wednesday":
        print("Midweek already,", name.capitalize() , "! Your", animal , "-like focus is impressive.")
    elif day == "thursday":
        print("Thursday's your day,", name.capitalize() , "! Your dedication to", hobby, "is inspiring.")
    elif day == "friday":
        print("Happy Friday,", name.capitalize() , "! Time to show off your", color, "style!")
    else:
        print("Enjoy your", day.capitalize() , ",", name.capitalize() , "! Your", animal, "energy is contagious!")

else:
    if day == "monday":
        print("Hello", name.capitalize() , "! Your", color, "outlook will make this Monday fantastic!")
    elif day == "tuesday":
        print("Happy Tuesday,", name.capitalize() , "! Your passion for", hobby, "will lead to great things.")
    elif day == "wednesday":
        print("Midweek motivation for", name.capitalize() , "! You're as unique as a", color, animal , ".")
    elif day == "thursday":
        print(name.capitalize() , ", your", animal , "-like determination will conquer this Thursday!")
    elif day == "friday":
        print("Fantastic Friday,", name.capitalize() , "! Celebrate with some", hobby, "time.")
    else:
        print("Have a wonderful", day.capitalize() , ",", name.capitalize() , "! Your", color, "spirit brightens everyone's day!")