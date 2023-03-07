number_of_employees = int(input('Введите кол-во сотрудников в офисе: '))
numbers = []
for id in range(number_of_employees):
    id = int(input('Введите ID сотрудника: '))
    numbers.append(id)

print(numbers)

search_ID = int(input('Какой ID ищем? '))
flag = False

for i in numbers:
     if i == search_ID:
         flag = True


if flag:
    print('Сотрудник на месте.')
else:
    print('Сотрудник не работает.')