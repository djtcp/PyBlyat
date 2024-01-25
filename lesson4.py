'''
first = int(input("Введите начало диапазона: "))
last = int(input("Введите конец диапазона: "))
count = 0
for num in range(first, last + 1):
    if num < 0:
        count += 1
print("Колличество отрицательных чисел в диапазоне :", count)
'''

first = int(input("Введите начало диапазона: "))
last = int(input("Введите конец диапазона: "))
count = 0
num = first
while num <= last:
    if num < 0:
        count += 1
    num += 1
print("Колличество отрицательных чисел в диапазоне, от", first, "до", last, "равно:", count)