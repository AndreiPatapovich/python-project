quantity_pack = int(input('Введите кол-во пакетов: '))

summ_list = []
pack_list = []

for i in range(quantity_pack):
    print(f'Пакет номер {i + 1}')
    for j in range(4):
        print(f'{j + 1} бит: ', end = '')
        num = int(input())
        pack_list.append(num)
    if pack_list.count(-1) <= 1:
        summ_list.extend(pack_list)

    pack_list = []
print(pack_list)
print(summ_list)
print(f'Число ошибок в списке {summ_list.count(-1)}')