'''
first = int(input("Введите начало диапазона: "))
last = int(input("Введите конец диапазона: "))
sum = 0
count = 0
for num in range(first, last + 1):
    sum += num
    count += 1
mean = sum / count
print("Среднее арифметическое число:", mean)
'''
first = int(input("Введите начало диапазона: "))
last = int(input("Введите конец диапазона: "))
sum = 0
count = 0
while first <= last:
    sum += first
    count += 1
    first += 1
mean = sum / count
print("Среднее арифметическое число:", mean)
