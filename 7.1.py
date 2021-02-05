class Matrix:

    def __init__(self, list_1, list_2,):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))


my_matrix = Matrix([[15, 49, 5],
                    [84, 87, 65],
                    [14, 2, 11]],
                   [[21, 35, 95],
                    [8, 3, 12],
                    [59, 56, 78]])

print(my_matrix.__add__())
