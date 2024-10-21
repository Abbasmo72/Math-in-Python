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

1. [Prime Numbers](MathPython/PrimeNumbers.py) : A prime number is a natural number greater than 1 that has only two divisors: 1 and itself. In other words, a prime number is divisible only by 1 and itself and cannot be expressed as the product of two smaller numbers. Prime numbers are crucial in number theory and have modern applications in fields like cryptography. Examples of prime numbers include 2, 3, 5, and 7. These numbers are often referred to as the "building blocks" of all natural numbers due to their unique properties.
<details>
<summary><b>More</b></summary>

This code defines a function called ispraime that checks whether a number is prime. The function first checks if the input number is less than or equal to 1, in which case it returns False because numbers less than 2 are not prime. Then, it uses a for loop to check all divisors from 2 to one less than the number. If the number is divisible by any of these values, it is not prime, and the function returns False. If no divisors are found, the function returns True, indicating the number is prime.

Next, the program takes an input from the user and passes it to the ispraime function. If the number is prime, it prints "prime"; otherwise, it prints "not prime."

## How it works:
1. The function receives a number.
2. If the number is less than 2, it is not prime.
3. For numbers greater than 1, it checks if the number is divisible by any number between 2 and itself minus one.
4. If divisible, the number is not prime; otherwise, it is prime

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

## License

MIT
