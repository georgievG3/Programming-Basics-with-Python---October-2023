budget = float(input())
season = input()

destination = ""
place = ""
holiday_price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        holiday_price = budget * 0.30
    elif season == "winter":
        place = "Hotel"
        holiday_price = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        holiday_price = budget * 0.40
    elif season == "winter":
        place = "Hotel"
        holiday_price = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    holiday_price = budget * 0.90
print(f"Somewhere in {destination}")
print(f"{place} - {holiday_price :.2f}")
