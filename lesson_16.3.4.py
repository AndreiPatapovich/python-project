
def matrix_num(matrix):

    for i_list in matrix:
        for i_num in i_list:
            print(i_num, end = ' ')
        print()

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_num(m)