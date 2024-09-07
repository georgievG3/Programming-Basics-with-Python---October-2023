day_of_the_week = input()
price_of_thicket = 0

if day_of_the_week == "Monday" \
        or day_of_the_week == "Tuesday" \
        or day_of_the_week == "Friday":
    price_of_thicket = 12
elif day_of_the_week == "Wednesday" \
        or day_of_the_week == "Thursday":
    price_of_thicket = 14
elif day_of_the_week == "Sunday" \
        or day_of_the_week == "Saturday":
    price_of_thicket = 16
print(price_of_thicket)
