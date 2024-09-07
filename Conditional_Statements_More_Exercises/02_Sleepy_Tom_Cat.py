WHOLE_YEAR = 365

rest_days = int(input())

working_days = WHOLE_YEAR - rest_days
working_play_time = working_days * 63  # minutes
rest_play_time = rest_days * 127  # minutes
total_play_time = working_play_time + rest_play_time  # minutes

extra_play = total_play_time - 30000
extra_play_hours = extra_play // 60
extra_play_minutes = extra_play % 60

less_play = 30000 - total_play_time
less_play_hours = less_play // 60
less_play_minutes = less_play % 60

if total_play_time > 30000:
    print("Tom will run away")
    print(f"{extra_play_hours} hours and {extra_play_minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{less_play_hours} hours and {less_play_minutes} minutes less for play")
