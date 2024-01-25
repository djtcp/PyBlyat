'''
list = [1, 2, 3, 4, 5]
listx = [x * 2 for x in list]
print(listx)
'''

list = [1, 2, 3, 4, 5]
element = 0

while element < len(list):
    list[element] *= 2
    element += 1
print(list)