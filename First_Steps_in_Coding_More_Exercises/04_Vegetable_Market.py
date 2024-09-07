vegetable_price_per_kg = float(input())
fruit_price_per_kg = float(input())
vegetable_kg = int(input())
fruit_kg = float(input())

vegetable_price = vegetable_price_per_kg * vegetable_kg
fruit_price = fruit_price_per_kg * fruit_kg

final_price_euro = (vegetable_price + fruit_price) / 1.94

print(f"{final_price_euro:.2f}")
