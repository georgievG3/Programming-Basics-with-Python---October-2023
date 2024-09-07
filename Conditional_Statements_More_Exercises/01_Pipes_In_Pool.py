volume = int(input())
first_pipe = int(input())
second_pipe = int(input())
hours_missing = float(input())

first_pipe_fill = first_pipe * hours_missing
second_pipe_fill = second_pipe * hours_missing
together_fill = first_pipe_fill + second_pipe_fill

percentage_filled = together_fill / volume * 100
first_pipe_percentage = first_pipe_fill / together_fill * 100
second_pipe_percentage = second_pipe_fill / together_fill * 100
liters_extra = together_fill - volume

if together_fill <= volume:
    print(f"The pool is {percentage_filled:.2f}% full. \
Pipe 1: {first_pipe_percentage:.2f}%. \
Pipe 2: {second_pipe_percentage:.2f}%.")
else:
    print(f"For {hours_missing:.2f} hours \
the pool overflows with {liters_extra:.2f} liters.")

