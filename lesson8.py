'''
import re

str = 'HelloSukaBlyad'
f_str = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', str)
print(f_str)
'''
str = 'HelloSukaBlyad'
element = 0
result = ''
while element < len(str):
    if str[element].isupper() and element != 0:
        result += ' '
    result += str[element]
    element += 1
print(result)