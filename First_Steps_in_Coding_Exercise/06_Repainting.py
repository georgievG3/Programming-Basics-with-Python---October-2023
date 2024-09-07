NYLON = 1.50
PAINT = 14.50
PAINT_THINNER = 5.00
BAGS = 0.40

needed_nylon = int(input())
needed_paint = int(input())
needed_pain_thinner = int(input())
hours = int(input())

final_nylon_price = (needed_nylon + 2) * NYLON
final_paint_price = (needed_paint + 0.10 * needed_paint) * PAINT
final_paint_thinner_price = needed_pain_thinner * PAINT_THINNER

cost_of_materials = final_nylon_price + final_paint_price + final_paint_thinner_price + BAGS
workers_pay_per_hour = (cost_of_materials * 0.30)
final_workers_pay = workers_pay_per_hour * hours

final_price = cost_of_materials + final_workers_pay

print(final_price)
