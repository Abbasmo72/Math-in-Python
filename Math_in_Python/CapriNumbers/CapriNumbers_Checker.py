def is_Capri(n):
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
    
    # Check the Capri condition
    return left_part + right_part == n

# Get user input
try:
    number = int(input("Enter a number to check if it is a Capri number: "))
    if is_Capri(number):
        print(f"{number} is a Capri number.")
    else:
        print(f"{number} is not a Capri number.")
except ValueError:
    print("Please enter a valid integer.")
