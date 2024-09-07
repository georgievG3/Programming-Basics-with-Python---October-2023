# age = float(input())
# gender = input()
#
# if gender == "m" and age >= 16:
#     print("Mr.")
# elif gender == "m" and age < 16:
#     print("Master")
# elif gender == "f" and age >= 16:
#     print("Ms.")
# elif gender == "f" and age < 16:
#     print("Miss")
#

ages = float(input())
gender = input()
if gender == "m":
    if ages >= 16:
        print("Mr.")
    else:
        print("Master")
elif gender == "f":
    if ages >= 16:
        print("Ms.")
    else:
        print("Miss")
