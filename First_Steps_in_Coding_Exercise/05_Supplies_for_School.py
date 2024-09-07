PENS = 5.80
MARKERS = 7.20
CLEANING_DETERGENT = 1.20

amount_pens = int(input()) * PENS
amount_markers = int(input()) * MARKERS
litres_of_cleaning_detergent = int(input()) * CLEANING_DETERGENT
discount_percentage = int(input()) / 100

price_for_all_materials = amount_pens + amount_markers + litres_of_cleaning_detergent

final_price = price_for_all_materials - (price_for_all_materials * discount_percentage)

print(final_price)

