resistance = 12.5

record_in_seconds = float(input())
distance_in_meters = float(input())
one_meter_time_in_seconds = float(input())

slow = distance_in_meters // 15 * resistance
total_time = distance_in_meters * one_meter_time_in_seconds + slow

if total_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time :.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_in_seconds :.2f} seconds slower.")
