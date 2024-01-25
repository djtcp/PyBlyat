'''
result = 1
for number in range(-127, 51):
    if number < 0 and number % 2 == 0:
        result *= number

print("Результат умножения отрицательно-четных чисел:", result)
'''
result = 1
number = -127

while number <= 50:
    if number < 0 and number % 2 == 0:
        result *= number
    number += 1

print("Результат умножения отрицательно-четных чисел:", result)