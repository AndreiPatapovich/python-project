while True:

    goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
    new_list = []

    new_fruit = input('Новый фрукт: ')
    new_list.append(new_fruit)

    prace = int(input('Цена: '))
    new_list.append(prace)

    goods.append(new_list)
    print(f'Старый ассортимент: {goods}')

    for i in goods:
        for j in i:
            if j == i[1]:
                j = j + j * 0.08
                i[1] = j
    print(f'Новый ассортимент: {goods}')