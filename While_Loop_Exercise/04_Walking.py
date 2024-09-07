STEPS_GOAL = 10000
step_counter = 0

while step_counter < STEPS_GOAL:
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        step_counter += steps_to_home
        break
    else:
        steps = int(command)
        step_counter += steps
steps_over = step_counter - STEPS_GOAL
if step_counter >= STEPS_GOAL:
    print("Goal reached! Good job!")
    print(f"{steps_over} steps over the goal!")
else:
    print(f"{-steps_over} more steps to reach goal.")
