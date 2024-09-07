record = float(input())
distance = float(input())
seconds_for_one_meter = float(input())

distance_in_seconds = distance * seconds_for_one_meter
slow_time = (distance // 50) * 30
total_time = distance_in_seconds + slow_time

if total_time >= record:
    print(f"No! He was {total_time - record:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
