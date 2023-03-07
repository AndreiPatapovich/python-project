nums_list = []

amount_of_numbers = int(input('Кол-во чисел в списке: '))

for number in range(amount_of_numbers):
    print('Введите', number + 1, end = '')
    num = int(input(' число: '))

    nums_list.append(num)

k_dell = int(input('Введите делитель: '))
count_ind = -1
summ = 0
for i in nums_list:
    count_ind += 1
    if i % k_dell == 0:
        summ += count_ind
        print('Индекс числа', i ,':', count_ind)

print('Сумма индексов: ', summ)
