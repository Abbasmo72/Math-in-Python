def is_kaprekar(n):
    # Calculate the square of the number
    square = n ** 2
    str_square = str(square)
    
    # Calculate the length of the number
    d = len(str(n))
    
    # Split the number into two parts
    left_part = str_square[:-d] if str_square[:-d] else '0'
    right_part = str_square[-d:]
    
    # Convert parts to integers
    left_part = int(left_part)
    right_part = int(right_part)
    
    # Check the Kaprekar condition
    return left_part + right_part == n

# Get user input
try:
    number = int(input("Enter a number to check if it is a Kaprekar number: "))
    if is_kaprekar(number):
        print(f"{number} is a Kaprekar number.")
    else:
        print(f"{number} is not a Kaprekar number.")
except ValueError:
    print("Please enter a valid integer.")
