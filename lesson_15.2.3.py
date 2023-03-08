line = input('Введите строку: ')
line_list = []
corrected_line = []

line_list = list(line)
count_symb = 0

for i in line_list:
    if i == ':':
        i = ';'
        count_symb += 1
    corrected_line.append(i)

#print(line_list)
print('Исправленная строка:')
for i in corrected_line:
    print(i, end = '')
print('\nКол-во исправлений:', count_symb)