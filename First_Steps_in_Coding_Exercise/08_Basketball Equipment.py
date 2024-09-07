year_tax_for_trainings = int(input())

basketball_shoes = year_tax_for_trainings - (year_tax_for_trainings * 0.40)
basketball_clothes = basketball_shoes - (basketball_shoes * 0.20)
basketball_ball = 0.25 * basketball_clothes
basketball_accessories = 0.20 * basketball_ball

final_price = year_tax_for_trainings \
              + basketball_shoes \
              + basketball_clothes \
              + basketball_ball \
              + basketball_accessories

print(final_price)
