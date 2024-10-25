<div align="center">

## Math in Python

<img alt="Gif" src="https://cdn.dribbble.com/users/31818/screenshots/1891002/math.gif" height="150px" width="500px">
</div>
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
 



## License

MIT
