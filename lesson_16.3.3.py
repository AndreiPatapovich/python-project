
first_word = input("Первое сообщение: ")
second_word = input("Первое сообщение: ")
first_count = first_word.count("!") + first_word.count("?")
second_count = second_word.count("!") + second_word.count("?")
if first_count < second_count:
    first_word, second_word = second_word, first_word  # пусть первым словом будет то, в котором больше знаков

print(first_word + second_word)