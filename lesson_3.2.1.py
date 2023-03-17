umber_of_employees = int(input('Кол-во сотрудников: '))
salaries_list = []
# print(f'Количество сотрудников: {umber_of_employees}')
for i in range(umber_of_employees):
    print('Зарплата', i + 1, 'сотрудника', end = ': ')
    salary = int(input(''))
    salaries_list.append(salary)

print(salaries_list)

for ind in salaries_list:
    if ind == 0:
        salaries_list.remove(ind)
        umber_of_employees -= 1
print(f'зарплаты: {salaries_list}')
print(f'Осталось сотрудников: {umber_of_employees} .')

print(f'Максимальная зарплата сотрудников: {max(salaries_list)}')
print(f'Минимальная зарплата сотрудников: {min(salaries_list)}')