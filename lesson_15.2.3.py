line_list = []
text_line = []
index = [0, 0, 0]

for i in range(3):
    print('Введите ', i + 1, 'слово: ', end = '')
    word = input()
    line_list.append(word)

text = input('Слово из текста: ')
text_line.append(text)

while text != 'end':
    text = input('Слово из текста: ')
    text_line.append(text)

print('Подсчет слов из текста')

for ind in text_line:
    if line_list[0] == ind:
        index[0] += 1
    if line_list[1] == ind:
        index[1] += 1
    if line_list[2] == ind:
        index[2] += 1

print(line_list)
print(text_line)
print(index)

for i in range(3):
    print(line_list[i], ':', index[i])

