PRICE_90X130 = 110
PRICE_100X150 = 140
PRICE_130X180 = 190
PRICE_200X300 = 250

windows_count = int(input())
type_of_windows = input()
shipment_method = input()

if windows_count < 10:
    print("Invalid order")
else:
    total_price = 0
    if type_of_windows == "90X130":
        total_price = windows_count * PRICE_90X130
        if 30 < windows_count < 60:
            total_price *= (1 - 0.05)
        elif windows_count >= 60:
            total_price *= (1 - 0.08)
    if type_of_windows == "100X150":
        total_price = windows_count * PRICE_100X150
        if 40 < windows_count < 80:
            total_price *= (1 - 0.06)
        elif windows_count >= 80:
            total_price *= (1 - 0.10)
    if type_of_windows == "130X180":
        total_price = windows_count * PRICE_130X180
        if 20 < windows_count < 50:
            total_price *= (1 - 0.07)
        elif windows_count >= 50:
            total_price *= (1 - 0.12)
    if type_of_windows == "200X300":
        total_price = windows_count * PRICE_200X300
        if 25 < windows_count < 50:
            total_price *= (1 - 0.09)
        elif windows_count >= 50:
            total_price *= (1 - 0.14)

    if shipment_method == "With delivery":
        total_price += 60

    if windows_count > 99:
        total_price *= (1 - 0.04)

    print(f"{total_price:.2f} BGN")
