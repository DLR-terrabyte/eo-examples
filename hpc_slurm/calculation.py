import sys
import time

# Check if a number is provided as a command-line argument
if len(sys.argv) != 2:
    print("ERROR:No input provided! Usage: python example.py <input_number>", file=sys.stderr)
    sys.exit(1)

# Get the input number from the command-line argument
try:
    user_input = float(sys.argv[1])
except ValueError:
    print("ERROR: Invalid input. Please provide a valid number.", file=sys.stderr)
    sys.exit(1)

# Perform a simple calculation (and make it a little bit longer) ;-)
result = user_input * 2
time.sleep(60)

# Print the result
print(f"The result of the calculation is: {result}")

