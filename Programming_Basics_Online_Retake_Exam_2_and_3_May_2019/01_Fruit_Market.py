strawberry_price = float(input())
banana_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberry_kg = float(input())

raspberries_price = strawberry_price / 2
orange_price = raspberries_price - (0.40 * raspberries_price)
banana_price = raspberries_price - (0.80 * raspberries_price)

total_strawberries = strawberry_kg * strawberry_price
total_raspberries = raspberries_kg * raspberries_price
total_banana = banana_price * banana_kg
total_orange = orange_price * oranges_kg

total_price = total_orange + total_banana + total_raspberries + total_strawberries

print(f"{total_price:.2f}")
