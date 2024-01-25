'''
first = int(input("Введите начало диапазона: "))
last = int(input("Введите конец диапазона: "))
sum = 0

for num in range(first,last + 1):
    sum += num
print("Сумма чисел в диапазоне ", "от", first, "до" , last, "равна:", sum)
'''


first = int(input("Введите начало диапазона: "))
last = int(input("Введите конец диапазона: "))

sum = 0
num = first

while num <= last:
    sum += num
    num += 1

print("Сумма чисел в диапазоне , от", first, "до" , last, "равна:", sum)