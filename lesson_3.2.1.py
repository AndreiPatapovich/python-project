zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
print(zoo)
zoo.insert(1, 'bear')
print(zoo)
zoo.remove('elephant')
print(zoo)
print('Лев сидит в клетке номер ', zoo.index('lion') + 1)
print('Обезьяна сидит в клетке номер ', zoo.index('monkey') + 1)