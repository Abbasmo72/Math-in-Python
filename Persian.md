<div align="center">

## ریاضی در پایتون

<img alt="Gif" src="https://cdn.dribbble.com/users/31818/screenshots/1891002/math.gif" height="150px" width="500px">
</div>
<hr>

link to read me
<hr>
ریاضیات در پایتون نقش مهمی در محاسبات و حل مسائل علمی یا مهندسی دارد. پایتون توابع و کتابخانه های داخلی را فراهم می کند که انجام طیف گسترده ای از عملیات ریاضی را از محاسبات اولیه تا محاسبات پیچیده تر آسان می کند. برای عملیات ساده، می توان از عملگرهای رایج مانند جمع، تفریق، ضرب و تقسیم استفاده کرد. علاوه بر این، پایتون دارای کتابخانه هایی مانند ریاضی برای توابع ریاضی عمومی، numpy برای عملیات بردار و ماتریس، و scipy برای محاسبات علمی پیشرفته است. این قابلیت‌ها به‌طور گسترده در زمینه‌هایی مانند تجزیه و تحلیل داده‌ها، یادگیری ماشین و مدل‌سازی مورد استفاده قرار می‌گیرند و به دلیل سادگی و قدرت محاسباتی پایتون را به ابزاری مورد علاقه در میان دانشمندان و مهندسان داده تبدیل می‌کنند .

## کتابخانه های مرتبط با ریاضی را نصب کنید

1. برای پایتون (با استفاده از پیپ):
```bash
pip install numpy scipy sympy matplotlib
```
- <b>NumPy:</b> برای عملیات ماتریسی و محاسبات عددی
- <b>SciPy:</b> برای محاسبات علمی و ریاضیات پیشرفته
- <b>SymPy:</b> برای جبر نمادین
- <b>Matplotlib:</b> برای رسم نمودارها
2. برای اوبونتو/دبیان (کتابخانه های سیستم مربوط به ریاضی):
```bash
sudo apt-get install libgsl-dev liblapack-dev libblas-dev
```
- <b>GSL:</b> کتابخانه علمی گنو برای محاسبات ریاضی
- <b>LAPACK/BLAS:</b> کتابخانه‌هایی برای حل معادلات خطی و سایر کارهای ریاضی
  
<details>
<summary><b>بیشتر</b></summary>
  
## ریاضیات در پایتون
پایتون به عنوان یک زبان برنامه نویسی همه کاره و قدرتمند، دارای طیف وسیعی از کاربردها در زمینه ریاضیات است. سادگی، خوانایی و پشتیبانی گسترده از کتابخانه آن را به ابزاری ارجح برای برنامه نویسان مبتدی و ریاضیدانان با تجربه تبدیل کرده است. پایتون چارچوبی را برای انجام انواع محاسبات ریاضی از محاسبات اولیه تا عملیات ریاضی پیشرفته فراهم می کند.

## محاسبات پایه در پایتون
پایتون در هسته خود از عملیات حسابی اساسی مانند جمع (+)، تفریق (-)، ضرب (*)، تقسیم (/)، و توان (**) پشتیبانی می کند. این عملیات برای هر زبان برنامه نویسی اساسی است، اما نحو واضح پایتون انجام محاسبات را آسان و شهودی می کند. پایتون را می توان برای مدیریت هر دو اعداد صحیح و اعداد ممیز شناور مورد استفاده قرار داد، که اجازه می دهد انواع سطوح دقیق در محاسبات را انجام دهد. به عنوان مثال، می توان به سرعت معادلات ساده ای مانند:
```python
result = (5 + 3) * 2
print(result)  # Output: 16
```

## ماژول ریاضی پایتونبرای کارهای پیچیده‌تر ریاضی، پایتون شامل ماژول ریاضی داخلی است که توابعی را برای ثابت‌ها و عملیات‌های ریاضی ارائه می‌کند. این ماژول به کاربران اجازه می دهد تا توابع مثلثاتی (sin()، cos() و غیره)، توابع لگاریتمی (log()، log10()) و فاکتوریل ها (factorial()) را انجام دهند. به عنوان مثال:
```python
import math
result = math.sqrt(16)
print(result)  # Output: 4.0
```
این ماژول قابلیت های بومی پایتون را گسترش می دهد و آن را برای مسائل مختلف ریاضی در دنیای واقعی که به توابع ریاضی سطح بالاتری نیاز دارند، مناسب می کند.

## محاسبات علمی با NumPy
در حالی که ماژول ریاضی توابع ریاضی ساده را مدیریت می کند، محاسبات پیشرفته تری - به ویژه آنهایی که شامل مجموعه داده های بزرگ یا آرایه های چند بعدی هستند - با کتابخانه NumPy امکان پذیر است. NumPy برای کارهایی مانند عملیات ماتریس، تبدیل فوریه و تولید اعداد تصادفی ضروری است. همچنین ستون فقرات اکثر برنامه نویسی های علمی و ریاضی در پایتون است. در اینجا مثالی از ایجاد یک آرایه و انجام عملیات اساسی با NumPy آورده شده است:
```python
import numpy as np
array = np.array([1, 2, 3, 4])
print(np.mean(array))  # Output: 2.5
```
NumPy به طور گسترده در زمینه هایی مانند یادگیری ماشین، علم داده و فیزیک استفاده می شود، جایی که مدل های ریاضی اغلب بر مجموعه داده های عددی بزرگ متکی هستند.

## ریاضیات نمادین با SymPy
برای دستکاری جبری و ریاضیات نمادین، پایتون SymPy را ارائه می دهد. این کتابخانه امکان محاسبه نمادین عبارات جبری را فراهم می کند که می تواند در حساب دیفرانسیل و انتگرال، جبر و حل معادلات مفید باشد. برخلاف محاسبات عددی، ریاضیات نمادین نمادها را به جای اعداد دستکاری می‌کنند و امکان نمایش دقیق معادلات را فراهم می‌کنند. به عنوان مثال، حل معادلات جبری به صورت نمادین به این صورت است:
```python
from sympy import symbols, Eq, solve
x = symbols('x')
equation = Eq(x**2 - 5*x + 6, 0)
solutions = solve(equation)
print(solutions)  # Output: [2, 3]
```
SymPy به ویژه در حوزه هایی مانند مهندسی و فیزیک نظری که در آن راه حل های نمادین دقیق مورد نیاز است مفید است.

## محاسبات علمی پیشرفته با SciPy
یک کتابخانه قدرتمند دیگر، SciPy، بر اساس NumPy ساخته شده است و قابلیت های اضافی را برای محاسبات علمی، از جمله ماژول هایی برای بهینه سازی، ادغام، درون یابی، مشکلات ارزش ویژه و موارد دیگر ارائه می دهد. SciPy بسیار کارآمد است و معمولاً در زمینه هایی مانند پردازش سیگنال و بیوانفورماتیک استفاده می شود.

## کاربردهای واقعی ریاضیات در پایتونقابلیت های ریاضی پایتون فراتر از مسائل آکادمیک است. در دنیای واقعی، پایتون برای برنامه های کاربردی مختلف استفاده می شود، از جمله:
- <b>علوم داده:</b> کتابخانه های پایتون مانند پانداها، matplotlib و NumPy به تجزیه و تحلیل مجموعه داده های بزرگ با استفاده از روش های آماری و ریاضی کمک می کنند.
- <b>یادگیری ماشین:</b> کتابخانه‌هایی مانند scikit-learn و TensorFlow از قدرت محاسباتی ریاضی پایتون برای آموزش مدل‌های یادگیری ماشینی استفاده می‌کنند که اغلب بر مفاهیم ریاضی مانند جبر خطی، حساب دیفرانسیل و انتگرال، و احتمال متکی هستند.
- <b>مالی:</b> پایتون معمولاً برای مدل‌سازی و شبیه‌سازی مالی استفاده می‌شود، جایی که به محاسبه الگوریتم‌های پیچیده و مدل‌های ریاضی برای سرمایه‌گذاری و تحلیل ریسک کمک می‌کند.
- <b>فیزیک و مهندسی:</b> پشتیبانی پایتون از محاسبات ریاضی به شبیه سازی سیستم های فیزیکی و حل مسائل مهندسی که شامل معادلات دیفرانسیل و بهینه سازی است کمک می کند.

## نتیجه گیری
در نتیجه، تطبیق پذیری و پشتیبانی گسترده از کتابخانه پایتون، آن را به زبانی بسیار مؤثر برای محاسبات ریاضی تبدیل کرده است. چه در حال انجام محاسبات پایه ای، ریاضیات نمادین یا محاسبات علمی پیشرفته باشید، سهولت استفاده و مقیاس پذیری پایتون طیف وسیعی از کاربردها را در تحقیقات، مهندسی، علوم داده و فراتر از آن امکان پذیر می کند.

</details>
<hr>

## اعداد اول


1. [عدد اول بین 0- 99](Math_in_Python/PrimeNumbers/PrimeNumber0-99.py) : این کد پایتون دو تابع را تعریف می کند: ispraime(n) و list_primes(). تابع ispraime() با اطمینان از بزرگتر بودن عدد n و نداشتن مقسوم علیه های دیگری به جز 1 و خودش، بررسی می کند که آیا عدد معین n اول است. تابع list_primes() در بین اعداد از 0 تا 99 تکرار می شود و از ispraime() برای تعیین و چاپ اعداد اول استفاده می کند. هنگامی که list_primes() اجرا می شود، تمام اعداد اول زیر 100 را نمایش می دهد.
   
<details>
<summary><b>بیشتر</b></summary>
  
## نحوه کار کد:
1. <b>تابع ispraime(n):</b>
   - <b>شماره ورودی را بررسی کنید:</b> اگر n کمتر یا مساوی 1 باشد، False را برمی‌گرداند زیرا اول نیست.
   - <b>بررسی بخش پذیری:</b> اگر هر عددی بین 2 و n-1 n را بدون باقیمانده تقسیم کند، False را برمی گرداند (که نشان می دهد n اول نیست).
   - <b>برگرداندن نتیجه:</b> اگر هیچ عددی n را تقسیم نکند، تابع True را برمی‌گرداند (که نشان می‌دهد n اول است).
2. <b>تابع list_primes():</b>
  - <b>تکرار از 0 تا 99:</b> این تابع در اعداد از 0 تا 99 حلقه می‌زند.
  - <b>Call ispraime():</b> برای هر عدد، اول بودن یا نبودن آن را بررسی می کند.
  - <b>چاپ اعداد اول:</b> اگر عددی اول باشد، عدد را چاپ می‌کند.
3. <b>اجرای نهایی:</b>
  تابع list_primes() فراخوانی می شود که تمام اعداد اول کمتر از 100 را چاپ می کند.

## کد پایتون
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

2. [چک کردن عدد اول](Math_in_Python/PrimeNumbers/Prime_Checker.py) : عدد اول یک عدد طبیعی بزرگتر از 1 است که فقط دو مقسوم علیه دارد: 1 و خودش. به عبارت دیگر، یک عدد اول فقط بر 1 و خودش بخش پذیر است و نمی توان آن را به صورت حاصل ضرب دو عدد کوچکتر بیان کرد. اعداد اول در نظریه اعداد بسیار مهم هستند و کاربردهای مدرنی در زمینه هایی مانند رمزنگاری دارند. نمونه هایی از اعداد اول عبارتند از 2، 3، 5 و 7. این اعداد به دلیل ویژگی های منحصر به فردشان اغلب به عنوان "بلوک های سازنده" همه اعداد طبیعی شناخته می شوند.
<details>
<summary><b>بیشتر</b></summary>

این کد تابعی به نام ispraime را تعریف می کند که اول بودن یک عدد را بررسی می کند. تابع ابتدا بررسی می کند که عدد ورودی کمتر یا مساوی 1 باشد، در این صورت False را برمی گرداند زیرا اعداد کوچکتر از 2 اول نیستند. سپس از یک حلقه for برای بررسی همه مقسوم‌کننده‌ها از 2 تا یک کمتر از عدد استفاده می‌کند. اگر عدد بر هر یک از این مقادیر بخش پذیر باشد، عدد اول نیست و تابع False را برمی گرداند. اگر مقسوم‌کننده‌ای پیدا نشد، تابع True را برمی‌گرداند که عدد اول را نشان می‌دهد.
در مرحله بعد، برنامه یک ورودی از کاربر می گیرد و آن را به تابع ispraime ارسال می کند. اگر عدد اول باشد، "prime" را چاپ می کند. در غیر این صورت، "not prime" را چاپ می کند.

## چگونه کار می کند:
1. تابع یک عدد دریافت می کند.
2. اگر عدد کمتر از 2 باشد، عدد اول نیست.
3. برای اعداد بزرگتر از 1، بررسی می کند که آیا عدد بر هر عددی بین 2 و خودش منهای یک بخش پذیر است یا خیر.
4. اگر قابل بخش باشد، عدد اول نیست. در غیر این صورت، آن را اول است.

## کد پایتون
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




## License

MIT

