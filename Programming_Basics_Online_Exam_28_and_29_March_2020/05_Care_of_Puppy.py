dog_food_kg = int(input())

dog_food_in_grams = dog_food_kg * 1000
total_grams = 0
left_overs = dog_food_in_grams

command = input()
while command != "Adopted":
    food_grams = int(command)
    total_grams += food_grams
    left_overs -= food_grams

    command = input()

if total_grams <= dog_food_in_grams:
    print(f"Food is enough! Leftovers: {left_overs} grams.")
else:
    print(f"Food is not enough. You need {total_grams - dog_food_in_grams} grams more.")
