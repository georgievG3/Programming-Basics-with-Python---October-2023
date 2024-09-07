luggage_price = float(input())
luggage_kg = float(input())
days_until_travel = int(input())
luggage_count = int(input())

total_price = 0

if luggage_kg < 10:
    total_price += luggage_price * 0.20
elif 10 <= luggage_kg <= 20:
    total_price += luggage_price * 0.50
else:
    total_price += luggage_price

if days_until_travel > 30:
    total_price += total_price * 0.10
elif 7 <= days_until_travel <= 30:
    total_price += total_price * 0.15
elif days_until_travel < 7:
    total_price += total_price * 0.40

final_price = total_price * luggage_count
print(f"The total price of bags is: {final_price:.2f} lv. ")
