quantity_sport = int(input('Сколько человек: '))
commands = int(input('Кол-во человек в команде: '))

sport_list = []
N = 1
if quantity_sport % commands == 0:
  for i in range(quantity_sport // commands):
      sport_list.append(list(range(N, N + commands)))
      N += commands
  print(f'Общий список комманд: {sport_list}')
else:
    print(f'{quantity_sport} участников нельзя раделить на команды по {commands} человек(а).')

