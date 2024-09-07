days = int(input())
total_food = float(input())

total_eaten_dog_food = 0
total_eaten_cat_food = 0
total_eaten_food = 0
biscuit = 0

days_count = 0
for day in range(1, days + 1):
    eaten_food_today = 0
    eaten_dog_food = float(input())
    eaten_cat_food = float(input())
    days_count += 1
    total_eaten_dog_food += eaten_dog_food
    total_eaten_cat_food += eaten_cat_food
    total_eaten_food += eaten_cat_food + eaten_dog_food
    eaten_food_today += eaten_cat_food + eaten_dog_food

    if days_count % 3 == 0:
        biscuit += eaten_food_today * 0.10

print(f"Total eaten biscuits: {round(biscuit)}gr.")
print(f"{total_eaten_food / total_food * 100:.2f}% of the food has been eaten.")
print(f"{total_eaten_dog_food / total_eaten_food * 100:.2f}% eaten from the dog.")
print(f"{total_eaten_cat_food / total_eaten_food * 100:.2f}% eaten from the cat.")
