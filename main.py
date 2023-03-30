
def is_polindrom(num_list):
    revers_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        revers_list.append(num_list[i_num])
    if num_list == revers_list:
        return True
    else:
        return False

nums = [1]
new_nums = []
answer = []

for i_nums in range(0, len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    if is_polindrom(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []
print(f'Исходный список {nums}')
print(f'Нужно добавить {len(answer)}')
print(f'Список чисел {answer}')