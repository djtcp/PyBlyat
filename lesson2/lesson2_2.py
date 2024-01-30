#Создаем функцию
def swap_case(string):
    #Создаем пустую строку куда пишем результат цикла
    str = ''

    # Инициализируем счетчик
    count = 0
    #запускаем цикл пока не достигнет конца строки
    while count < len(string):
        # меняем нижний регистр на верхний
        if string[count].islower():
            str += string[count].upper()
        # меняем верний регистр на нижний
        elif string[count].isupper():
            str += string[count].lower()
        else:
            # Добавляем символ без изменений, если это не буква
            str += string[count]
        # Увеличиваем счетчик
        count += 1
    # Возвращаем получившуюся строку
    return str

#Строка для выполнения
str = 'SuKaBlEaTsUkAbLeAtSuKaBlEaTsUkAbLeAt'

#Вызываем функцию
new_str = swap_case(str)

#Выводи результат
print(new_str)