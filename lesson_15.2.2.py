nums_list = []

amount_of_dogs = int(input('Кол-во собак в соревнованиях: '))

for dog in range(amount_of_dogs):
    print(dog + 1 ,'-я собака -', end = '')
    num = int(input(' кол-во очков: '))

    nums_list.append(num)

print(f'Первоначальный список {nums_list}')
first_dog = nums_list[0]
last_dog = nums_list[amount_of_dogs - 1]

for dog in range(amount_of_dogs ):
    if dog == 0:
        last_dog = nums_list[0]
    if dog == amount_of_dogs - 1:
        first_dog = nums_list[amount_of_dogs - 1]

nums_list[0] = first_dog
nums_list[amount_of_dogs -1] = last_dog
print(f'Конечный список {nums_list}')