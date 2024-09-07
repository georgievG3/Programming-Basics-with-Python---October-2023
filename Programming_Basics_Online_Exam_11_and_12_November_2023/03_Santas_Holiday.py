ROOM_FOR_ONE_PRICE = 18
APARTMENT_PRICE = 25
PRESIDENT_APARTMENT_PRICE = 35

days_stay = int(input())
type_of_room = input()
review = input()

stay_price = 0
if type_of_room == "room for one person":
    stay_price = (days_stay - 1) * ROOM_FOR_ONE_PRICE
elif type_of_room == "apartment":
    stay_price = (days_stay - 1) * APARTMENT_PRICE
    if days_stay < 10:
        stay_price = stay_price * (1 - 0.30)
    elif 10 <= days_stay <= 15:
        stay_price = stay_price * (1 - 0.35)
    elif days_stay > 15:
        stay_price = stay_price * (1 - 0.50)
elif type_of_room == "president apartment":
    stay_price = (days_stay - 1) * PRESIDENT_APARTMENT_PRICE
    if days_stay < 10:
        stay_price = stay_price * (1 - 0.10)
    elif 10 <= days_stay <= 15:
        stay_price = stay_price * (1 - 0.15)
    elif days_stay > 15:
        stay_price = stay_price * (1 - 0.20)

if review == "positive":
    stay_price = stay_price * (1 + 0.25)
else:
    stay_price = stay_price * (1 - 0.10)

print(f"{stay_price:.2f}")
