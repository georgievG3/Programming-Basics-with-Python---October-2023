from math import floor, ceil

space = int(input())
kg_grapes_per_square_meter = float(input())
needed_litres_wine = int(input())
workers = int(input())

harvest = space * 0.40
total_grapes = harvest * kg_grapes_per_square_meter
total_litre_wine = total_grapes / 2.5
extra_wine = total_litre_wine - needed_litres_wine
worker_cut = extra_wine / workers

if needed_litres_wine > total_litre_wine:
    print(f"It will be a tough winter! More {floor(-extra_wine)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(total_litre_wine)} liters.")
    print(f"{ceil(extra_wine)} liters left -> {ceil(worker_cut)} liters per person.")
