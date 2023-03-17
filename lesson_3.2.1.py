def is_film_exist(movie, film_list):
    for i_movie in film_list:
        if i_movie == movie:
            return True
    return False


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня',
         'Проклятый остров', 'Начало', 'Матрица']

my_list = []
while True:

    print(f'\nВаш текущий топ фильмов {my_list}')
    new_film = input('Введите название фильма: ')
    if is_film_exist(new_film, films):
        print('Команды: добавить, вставить, удалить')
        command = input('Введите команду: ')
        if command == 'добавить':
            my_list.append(new_film)
        if command == 'вставить':
            index = int(input('На какое место вставить? '))
            my_list.insert(index - 1, new_film)
        if command == 'удалить':
            if is_film_exist(new_film, my_list):
                 my_list.remove(new_film)
            else:
                print('Такого фильма нет в топе.')

    else:
        print('Такого фильма нет на сайте.')

