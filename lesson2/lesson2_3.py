orig_list = [5, 1, 89, 2, 3, 4, 0]
mod_list = []

for num in orig_list:
    if num % 2 == 0:  # Проверяем на четное число
        mod_list.append(num * 2)  # умножаем четные числа на 2
    else:
        mod_list.append(num) # Добавляем нечетные элемнты без умножения
# сортируем новый список
sort_list = sorted(mod_list)
# Выводим результат
print(sort_list)