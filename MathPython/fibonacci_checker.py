import math

# Function to check if a number is a perfect square
def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

# Function to check if the input number is a Fibonacci number
def is_fibonacci(n):
    # Checking Fibonacci condition
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Input a number from the user
num = int(input("Enter a number: "))

# Displaying the result
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is not a Fibonacci number.")
