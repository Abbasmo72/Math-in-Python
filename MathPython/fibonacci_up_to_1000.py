# Define the function to generate Fibonacci sequence up to 1000
def fibonacci_up_to_1000():
    a, b = 0, 1  # Starting values of the Fibonacci sequence
    while a <= 1000:
        print(a, end=' ')
        a, b = b, a + b  # Update the sequence

# Run the function to display Fibonacci numbers from 0 to 1000
fibonacci_up_to_1000()
