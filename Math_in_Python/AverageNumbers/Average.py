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