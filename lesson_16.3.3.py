main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]

first_company = [0, 0, 0]

second_company = [1, 0, 0, 1, 1]

third_company = [1, 1, 1, 0, 1]

main.extend(first_company + second_company + third_company)

a = main.count(0)
print(f'Общий список задач: {main}')
print(f'Кол-во невыполненных задач: {a}')
