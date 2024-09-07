days_to_stay = int(input())
type_of_room = input()
rating = input()

ROOM_FOR_ONE_PRICE = 18.00
APARTMENT_PRICE = 25.00
PRESIDENT_APARTMENT = 35.00

overnight_stay = days_to_stay - 1

room_cost = 0

if type_of_room == "room for one person":
    room_cost = ROOM_FOR_ONE_PRICE * overnight_stay
elif type_of_room == "apartment":
    room_cost = APARTMENT_PRICE * overnight_stay
    if days_to_stay < 10:
        room_cost *= 0.70
    elif 10 <= days_to_stay <= 15:
        room_cost *= 0.65
    elif days_to_stay > 15:
        room_cost *= 0.50
elif type_of_room == "president apartment":
    room_cost = PRESIDENT_APARTMENT * overnight_stay
    if days_to_stay < 10:
        room_cost *= 0.90
    elif 10 <= days_to_stay <= 15:
        room_cost *= 0.85
    elif days_to_stay > 15:
        room_cost *= 0.80

if rating == "positive":
    room_cost *= 1.25
elif rating == "negative":
    room_cost *= 0.90

print(f"{room_cost :.2f}")
