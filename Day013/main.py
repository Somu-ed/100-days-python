print("Exam Grade Calculator")
print("**********************")
print()

name_of_exam = input("Name of exam: ")
print()

total_score = int(input("Max. Possible Score: "))
your_score = int(input("Your score: "))
print()

final_perc = round((your_score / total_score) * 100, 2)

print("You got", final_perc, "%")

if final_perc >= 90:
    print("Your letter grade is O 🎉")
elif final_perc >= 80:
    print("Your letter grade is A 😃")
elif final_perc >= 70:
    print("Your letter grade is B 😊")
elif final_perc >= 60:
    print("Your letter grade is C 🙂")
elif final_perc >= 50:
    print("Your letter grade is D 😐")
elif final_perc >= 40:
    print("Your letter grade is E 😕")
else:
    print("Your letter grade is F 😢")

print("\nYou received a", final_perc, "% on your", name_of_exam, "exam.")