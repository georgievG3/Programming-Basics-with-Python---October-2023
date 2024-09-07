mackerel_price = float(input())
sprinkle_price = float(input())
bonito_kg = float(input())
scad_kg = float(input())
mussel_kg = float(input())

bonito_price = mackerel_price + (mackerel_price * 0.60)
scad_price = sprinkle_price + (sprinkle_price * 0.80)
mussel_price = mussel_kg * 7.50

total_price = (bonito_price * bonito_kg) \
              + (scad_price * scad_kg) \
              + mussel_price
print(f"{total_price:.2f}")
