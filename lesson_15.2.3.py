line = input('Введите строку: ')
number_symb = int(input('Введите номер символа: '))

line_list = []
line_list = list(line)

symbol = ''
left_symbol = line_list[number_symb - 2]
raigt_symbol = line_list[number_symb]

count_symb = -1
count = 0
for i in line_list:
    count_symb += 1
    if number_symb -1 == count_symb:
        symbol = i

for ind in line_list:
    if ind == symbol:
        count += 1

print('Символ слева: ', left_symbol)
print('Символ справа: ', raigt_symbol)

if count == 1:
    print(f'Таких же символов "{symbol}" больше нет в строке')
if count == 2:
    print(f'Есть ровно один такой же "{symbol}" символ')

