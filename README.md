<div align="center">

## Math in Python

<img alt="Gif" src="https://cdn.dribbble.com/users/31818/screenshots/1891002/math.gif" height="150px" width="500px">
</div>
<hr>

[Click to see the descriptions in Persian language](Persian.md)
<hr>
Mathematics in Python plays a crucial role in computations and solving scientific or engineering problems. Python provides built-in functions and libraries that make it easy to perform a wide range of mathematical operations, from basic arithmetic to more complex calculations. For simple operations, one can use common operators like addition, subtraction, multiplication, and division. Additionally, Python has libraries such as math for general mathematical functions, numpy for vector and matrix operations, and scipy for advanced scientific computations. These capabilities are extensively used in fields like data analysis, machine learning, and modeling, making Python a favorite tool among data scientists and engineers due to its simplicity and computational power.

## Install math-related libraries

1. For Python (using pip):
```bash
pip install numpy scipy sympy matplotlib
```
- <b>NumPy:</b> For matrix operations and numerical computations
- <b>SciPy:</b> For scientific computing and advanced mathematics
- <b>SymPy:</b> For symbolic algebra
- <b>Matplotlib:</b> For plotting graphs
2. For Ubuntu/Debian (system libraries related to math):
```bash
sudo apt-get install libgsl-dev liblapack-dev libblas-dev
```
- <b>GSL:</b> GNU Scientific Library for mathematical computations
- <b>LAPACK/BLAS:</b> Libraries for solving linear equations and other math tasks
  
<details>
<summary><b>More</b></summary>
  
## Mathematics in Python
Python, as a versatile and powerful programming language, has a wide array of applications in the field of mathematics. Its simplicity, readability, and extensive library support make it a preferred tool for both beginner programmers and experienced mathematicians. From basic arithmetic to advanced mathematical operations, Python provides a framework for handling diverse types of mathematical computations.

## Basic Arithmetic in Python
At its core, Python supports basic arithmetic operations such as addition (+), subtraction (-), multiplication (*), division (/), and exponentiation (**). These operations are fundamental to any programming language, but Python’s clear syntax makes performing calculations easy and intuitive. Python can be used to handle both integers and floating-point numbers, allowing for a variety of precision levels in computations. For example, one can quickly compute simple equations like:
```python
result = (5 + 3) * 2
print(result)  # Output: 16
```

## Python’s math Module
For more complex mathematical tasks, Python includes the built-in math module, which provides functions for mathematical constants and operations. This module allows users to perform trigonometric functions (sin(), cos(), etc.), logarithmic functions (log(), log10()), and factorials (factorial()), among others. For example:
```python
import math
result = math.sqrt(16)
print(result)  # Output: 4.0
```
This module extends Python’s native capabilities, making it suitable for various real-world mathematical problems that require higher-level mathematical functions.

## Scientific Computations with NumPy
While the math module handles simple mathematical functions, more advanced computations—especially those involving large datasets or multidimensional arrays—are made possible with the NumPy library. NumPy is essential for tasks like matrix operations, Fourier transforms, and random number generation. It is also the backbone of most scientific and mathematical programming in Python. Here’s an example of creating an array and performing basic operations with NumPy:

```python
import numpy as np
array = np.array([1, 2, 3, 4])
print(np.mean(array))  # Output: 2.5
```
NumPy is widely used in fields like machine learning, data science, and physics, where mathematical models often rely on large numerical datasets.

## Symbolic Mathematics with SymPy
For algebraic manipulation and symbolic mathematics, Python offers SymPy. This library allows for the symbolic computation of algebraic expressions, which can be useful in calculus, algebra, and equation solving. Unlike numerical computation, symbolic math manipulates symbols rather than numbers, allowing for the exact representation of equations. For instance, solving algebraic equations symbolically looks like this:
```python
from sympy import symbols, Eq, solve
x = symbols('x')
equation = Eq(x**2 - 5*x + 6, 0)
solutions = solve(equation)
print(solutions)  # Output: [2, 3]
```
SymPy is especially helpful in domains such as engineering and theoretical physics where precise symbolic solutions are required.

## Advanced Scientific Computing with SciPy
Another powerful library, SciPy, builds on NumPy and provides additional functionality for scientific computing, including modules for optimization, integration, interpolation, eigenvalue problems, and more. SciPy is highly efficient and is commonly used in fields such as signal processing and bioinformatics.

## Real-World Applications of Mathematics in Python
Python’s mathematical capabilities extend beyond academic problems. In the real world, Python is used for various applications, including:
- <b>Data Science:</b> Python’s libraries like pandas, matplotlib, and NumPy help analyze large datasets using statistical and mathematical methods.
- <b>Machine Learning:</b> Libraries such as scikit-learn and TensorFlow leverage Python’s mathematical computing power to train machine learning models, which often rely on mathematical       concepts like linear algebra, calculus, and probability.
- <b>Finance:</b> Python is commonly used for financial modeling and simulations, where it helps compute complex algorithms and mathematical models for investment and risk analysis.
- <b>Physics and Engineering:</b> Python’s support for mathematical computations aids in the simulation of physical systems and solving engineering problems that involve differential equations and optimization.

## Conclusion
In conclusion, Python’s versatility and extensive library support make it a highly effective language for mathematical computations. Whether you are performing basic arithmetic, symbolic mathematics, or advanced scientific computations, Python’s ease of use and scalability enable a wide range of applications in research, engineering, data science, and beyond.

</details>
<hr>

## Prime Numbers

1. [Prime Numbers 0- 99](Math_in_Python/PrimeNumbers/PrimeNumber0-99.py) : This Python code defines two functions: ispraime(n) and list_primes(). The ispraime() function checks if a given number n is prime by ensuring it's greater than 1 and has no divisors other than 1 and itself. The list_primes() function iterates through numbers from 0 to 99 and uses ispraime() to determine and print which numbers are prime. When list_primes() is executed, it displays all prime numbers below 100.
   
<details>
<summary><b>More</b></summary>
  
## How the Code Works:
1. <b>Function ispraime(n):</b>
   - <b>Check input number:</b> If n is less than or equal to 1, it returns False because it's not prime.
   - <b>Check divisibility:</b> If any number between 2 and n-1 divides n without a remainder, it returns False (indicating n is not prime).
   - <b>Return result:</b> If no numbers divide n, the function returns True (indicating n is prime).
2. <b>Function list_primes():</b>
  - <b>Iterating from 0 to 99:</b> This function loops through numbers from 0 to 99.
  - <b>Call ispraime():</b> For each number, it checks whether it is prime or not.
  - <b>Print prime numbers:</b> If a number is prime, it prints the number.
3. <b>Final Execution:</b>
  The list_primes() function is called, printing all prime numbers less than 100.

## Python Code
```python
def ispraime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True
    
def list_primes():
    for n in range(100):
        if ispraime(n):
            print(n, end=' ', flush=True)
    print()

list_primes()
```
</details>

2. [Prime Numbers Checker](Math_in_Python/PrimeNumbers/Prime_Checker.py) : A prime number is a natural number greater than 1 that has only two divisors: 1 and itself. In other words, a prime number is divisible only by 1 and itself and cannot be expressed as the product of two smaller numbers. Prime numbers are crucial in number theory and have modern applications in fields like cryptography. Examples of prime numbers include 2, 3, 5, and 7. These numbers are often referred to as the "building blocks" of all natural numbers due to their unique properties.
<details>
<summary><b>More</b></summary>

This code defines a function called ispraime that checks whether a number is prime. The function first checks if the input number is less than or equal to 1, in which case it returns False because numbers less than 2 are not prime. Then, it uses a for loop to check all divisors from 2 to one less than the number. If the number is divisible by any of these values, it is not prime, and the function returns False. If no divisors are found, the function returns True, indicating the number is prime.

Next, the program takes an input from the user and passes it to the ispraime function. If the number is prime, it prints "prime"; otherwise, it prints "not prime."

## How it works:
1. The function receives a number.
2. If the number is less than 2, it is not prime.
3. For numbers greater than 1, it checks if the number is divisible by any number between 2 and itself minus one.
4. If divisible, the number is not prime; otherwise, it is prime.

## Python Code
```python
def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True
    
n = int(input('Enter The Number: '))
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime')
```

</details>
<hr>

## Fibonacci Sequence
1. [Fibonacci Sequence 0-1000](Math_in_Python/FibonacciSequence/fibonacci_up_to_1000.py) : The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1. It goes like this: 0, 1, 1, 2, 3, 5, 8, and so on. This sequence has a wide range of applications in mathematics, computer science, biology, and even art, due to its appearance in various natural patterns and structures. The sequence is named after Italian mathematician Leonardo Fibonacci, who introduced it to Western mathematics in his 13th-century book Liber Abaci. Each number in the sequence is called a "Fibonacci number," and these numbers have unique mathematical properties.

<details>
<summary><b>More</b></summary>
  
## The History and Significance of Fibonacci Numbers

The history of Fibonacci numbers dates back to the 13th century when an Italian mathematician named Leonardo Fibonacci introduced this sequence in his famous book Liber Abaci. In the book, Fibonacci used the sequence to solve a problem related to the population growth of rabbits. In this sequence, each number is the sum of the two preceding ones, starting from 0 and 1. The series progresses as follows: 0, 1, 1, 2, 3, 5, 8, and so on. Over time, the significance of the Fibonacci sequence became widely recognized due to its applications in natural patterns and biological formations. Patterns like the golden ratio in plants, animals, and even galaxies correspond with the Fibonacci sequence, making Fibonacci and his sequence a fundamental part of mathematical history. This sequence has also influenced fields like architecture, music, and art, serving as a foundational structural and geometric framework in the world.

## How it works:
1. <b>Function Definition:</b> fibonacci_up_to_1000() is defined to generate Fibonacci numbers up to 1000.
2. <b>Initial Values:</b> Inside the function, the first two numbers of the Fibonacci sequence are set, a as 0 and b as 1.
3. <b>Loop Execution:</b> The while loop runs as long as a is less than or equal to 1000. Within the loop, it prints the current value of a, which is a Fibonacci number.
4. <b>Update of Variables:</b> After each print, the values of a and b are updated to move to the next Fibonacci number by setting a to b and b to a + b.
5. <b>Function Call:</b> Calling fibonacci_up_to_1000() runs the loop and outputs all Fibonacci numbers from 0 up to 1000 in a single line.

## Python Code
```python
# Define the function to generate Fibonacci sequence up to 1000
def fibonacci_up_to_1000():
    a, b = 0, 1  # Starting values of the Fibonacci sequence
    while a <= 1000:
        print(a, end=' ')
        a, b = b, a + b  # Update the sequence

# Run the function to display Fibonacci numbers from 0 to 1000
fibonacci_up_to_1000()
```

</details>
<hr>

2. [Fibonacci Check](Math_in_Python/FibonacciSequence/fibonacci_checker.py) : The code above is a simple program to check if a number is a Fibonacci number. It defines a function, is_perfect_square, which checks if a given number is a perfect square. This is useful for identifying Fibonacci numbers because of a specific mathematical property they hold. The main function, is_fibonacci, then uses a "Fibonacci condition" to determine if the input number is a Fibonacci number. According to this condition, a number n is a Fibonacci number if either 5 * n * n + 4 or 5 * n * n - 4 is a perfect square. Finally, the program prompts the user to input a number, and it uses the is_fibonacci function to display whether or not the number is part of the Fibonacci sequence.

<details>
<summary><b>More</b></summary>

This process efficiently confirms Fibonacci membership without needing to generate a sequence up to the number.

## How it works:
1. <b>Check if a Number is a Perfect Square:</b> The function is_perfect_square checks if a number is a perfect square by taking the square root of x, converting it to an integer, and checking if squaring this integer gives back the original number x. If it does, x is a perfect square.
2. <b>Determine if a Number is Fibonacci:</b> The function is_fibonacci determines whether a number n is a Fibonacci number. It uses a mathematical property where a number n is in the Fibonacci sequence if either 5 * n * n + 4 or 5 * n * n - 4 is a perfect square. This condition is derived from mathematical characteristics unique to Fibonacci numbers.
3. <b>User Input:</b> The program prompts the user to enter a number for testing, storing it as num.
4. <b>Check and Display Result:</b> Finally, the program checks if num is a Fibonacci number using the is_fibonacci function. It then prints the result, confirming whether num is or is not a Fibonacci number based on the function's output.

## Python Code
```python
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
```

</details>
<hr>

## Kaprekar Numbers
What are Kaprekar Numbers?
Kaprekar numbers are special numbers for which, when squared, the resulting number can be split into two parts that, when summed, equal the original number.
 
1. [Kaprekar Numbers 0-1000](Math_in_Python/KaprekarNumbers/KaprekarNumbers0_1000.py) : This program identifies and displays Kaprekar numbers from 0 to 1000. The is_kaprekar function is used to check if a given number is a Kaprekar number. The function squares the input number, then splits this square into two parts. If the sum of these two parts equals the original number, the function returns True, marking it as a Kaprekar number. The program then collects all such numbers within the specified range and prints them as output.
   
<details>
<summary><b>More</b></summary>


## How it works:
1. <b>Square Calculation:</b> The is_kaprekar function calculates the square of the input number 𝑛.
2. <b>String Conversion:</b> It converts the squared result into a string for easier splitting.
3. <b>Splitting the Square:</b> The string is divided into two parts, with the right part having the same number of digits as the original number 𝑛. If the left part is empty, it defaults to zero.
4. <b>Integer Conversion:</b> Both parts are converted back into integers.
5. <b>Kaprekar Condition Check:</b> The two parts are summed. If their sum matches the original number, then 𝑛 is considered a Kaprekar number.

## Python Code
```python
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

# Display Kaprekar numbers from 0 to 1000
kaprekar_numbers = [n for n in range(1001) if is_kaprekar(n)]
print("Kaprekar numbers from 0 to 1000:", kaprekar_numbers)
```

</details>
<hr>

2. [Kaprekar Numbers Checker](Math_in_Python/KaprekarNumbers/KaprekarNumbers_Checker.py) : This program takes a user input and checks if it is a Kaprekar number. The is_kaprekar function squares the input number, splits the square into two parts, and checks if the sum of these two parts equals the original number. If so, the number is identified as a Kaprekar number, and a corresponding message is displayed. The program also handles invalid inputs by showing an error message if the input is not a valid integer.

<details>
<summary><b>More</b></summary>

## How it works:
1. <b>Square Calculation:</b> The function squares the input number 𝑛.
2. <b>String Conversion:</b> It converts the square to a string for easy splitting.
3. <b>Splitting the Square:</b> The string is split into left and right parts, with the right part having the same number of digits as 𝑛. If the left part is empty, it defaults to zero.
4. <b>Integer Conversion:</b> Both parts are converted back to integers.
5. <b>Kaprekar Condition Check:</b> If the sum of the two parts equals 𝑛, the number is confirmed as a Kaprekar number.

## Python Code
```python
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
```

</details>
<hr>

## Geometric calculations
Geometric calculations study and analyze the characteristics of different geometric shapes. These calculations include measuring dimensions, area, perimeter and volume of two-dimensional and three-dimensional shapes. For each geometric shape, there are special formulas that can be used to calculate its properties.

1. [Circle Geometry](Math_in_Python/GeometricCalculations/CircleGeometry.py) : This code calculates the area and circumference of a circle based on its radius in centimeters. It defines a function that takes the radius as input and computes the area and circumference using mathematical formulas. The program then prompts the user to enter the circle's radius. The calculated results, including the area and circumference, are displayed in the console with precision.
   
<details>
<summary><b>More</b></summary>

## How it works:
1. Importing the Math Module: It uses import math to access mathematical functions.
2. Defining the Function: The calculate_circle function calculates the area and circumference using the formulas Area=𝜋𝑟2 Area=πr and Circumference=2𝜋𝑟.
3. Getting User Input: It uses input to get the radius of the circle from the user and converts it to a float.
4. Calculating and Displaying Results: The function is called to compute the area and circumference, which are then displayed with two decimal places.

## Python Code
```python
import math

# Function to calculate the area and circumference of a circle in centimeters
def calculate_circle(radius_cm):
    area_cm2 = math.pi * radius_cm ** 2  # Calculate area in square centimeters
    circumference_cm = 2 * math.pi * radius_cm  # Calculate circumference in centimeters
    return area_cm2, circumference_cm

# Get the radius from the user in centimeters
radius_cm = float(input("Enter the radius of the circle in centimeters: "))

# Calculate area and circumference
area_cm2, circumference_cm = calculate_circle(radius_cm)

# Display the results
print(f"Area of the circle: {area_cm2:.2f} cm²")  # Display area in square centimeters
print(f"Circumference of the circle: {circumference_cm:.2f} cm")  # Display circumference in centimeters
```
</details>
<hr>

2. [Rectangle Calculator](Math_in_Python/GeometricCalculations/RectangleCalculator.py) : Explanation in English: This code prompts the user to input the length and width of a rectangle. It then calculates the area by multiplying the length by the width and the perimeter by doubling the sum of the length and width. After performing these calculations, it displays the calculated area and perimeter values back to the user.

<details>
<summary><b>More</b></summary>

## How it works:
1. Get the length and width from the user and convert them to floating-point numbers.
2. Calculate the area by multiplying the length by the width.
3. Calculate the perimeter using the formula 2×(𝑙𝑒𝑛𝑔𝑡ℎ+𝑤𝑖𝑑𝑡ℎ)2×(length+width).
4. Display the calculated area and perimeter.

## Python Code
```python
# Get length and width from the user
length = float(input("Enter the rectangle's length: "))
width = float(input("Enter the rectangle's width: "))

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Display results
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)
```
</details>
<hr>

3. [Square Calculator](Math_in_Python/GeometricCalculations/SquareCalculator.py) : This code prompts the user to enter the side length of a square and converts it to a floating-point number. It then calculates the area by squaring the side length and finds the perimeter by multiplying the side length by 4. Finally, it displays the calculated area and perimeter to the user.

<details>
<summary><b>More</b></summary>

## How it works:
1. Get the side length of the square from the user and convert it to a floating-point number.
2. Calculate the area by squaring the side length.
3. Calculate the perimeter by multiplying the side length by 4.
4. Display the calculated area and perimeter.

## Python Code
```python
# Get the side length of the square from the user
side = float(input("Enter the side length of the square: "))

# Calculate area and perimeter
area = side * side
perimeter = 4 * side

# Display results
print("The area of the square is:", area)
print("The perimeter of the square is:", perimeter)
```
</details>
<hr>

## Averag Numbers
[Averag Number Code](Math_in_Python/AverageNumbers/Average.py) : Averaging is a process in which a central value is obtained from a set of data by summing the numbers and dividing the result by the count of values. The mean serves as an indicator to understand and summarize statistical information, making it highly useful in data analysis. This concept is important across various fields, including economics, social sciences, and engineering. There are different types of averages, such as arithmetic mean, weighted mean, and geometric mean, each used in specific contexts.

<details>
<summary><b>More</b></summary>

## How it works:
1. <b>Defining and Initializing Variables:</b> Two variables are defined: count to keep track of the number of inputs and sum to store the total sum of numbers. Both are initially set to zero.
2. <b>Getting Numbers from the User:</b> In a loop, the program prompts the user to enter a number. If the entered number isn’t -1:
   - It increments count by one,
   - Adds the number to sum.
3. <b>Ending the Loop and Calculating the Average:</b> When the user enters -1, the loop stops, and the program calculates the average by dividing sum by count.
4. <b>Displaying the Result:</b> The program then displays the total count, the sum, and the calculated average.

## Python Code
```python
import time
count = 0
sum = 0

print('''The program will take numbers from you until you type -1 
It calculates the number of numbers as well as the sum of the numbers and 
finally the average of the numbers.''')

time.sleep(1)
numbers = int(input('Enter Your Number : '))
while numbers != -1:
    count += 1
    sum += numbers
    numbers = int(input('Enter Your Number : '))
average = sum / count
time.sleep(1.5)
print(f'Number of numbers entered {count}')
print(f'The sum of the entered numbers {sum}')
print(f'The average of the entered numbers {average}')
```
</details>
<hr>


## License

MIT
