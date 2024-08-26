print("How many seconds are in a year?")
print("================================")

print()
year = int(input("Input a year: "))

if year % 4 == 0:
    days_in_year = 366
else:
    days_in_year = 365

hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

result = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

print()
if days_in_year == 366:
    print("Number of seconds in the leap year", days_in_year, " are", result)
else:
    print("Number of seconds in the year", days_in_year, " are", result)