import numpy as np


class Matrix:
    def __init__(self, data) -> None:
        self.data = data
        self.n_rows = len(data)
        self.n_cols = len(data[0])

    def __add__(self, matrix):
        if self.n_rows != matrix.n_rows:
            raise ValueError("Not equal number of rows")
        if self.n_cols != matrix.n_cols:
            raise ValueError("Not equal number of columns")

        matrix_sum = Matrix(
            [[0 for _ in range(self.n_cols)] for _ in range(self.n_rows)]
        )

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                matrix_sum.data[i][j] = self.data[i][j] + matrix.data[i][j]

        return matrix_sum

    def __mul__(self, matrix):
        if self.n_rows != matrix.n_rows:
            raise ValueError("Not equal number of rows")
        if self.n_cols != matrix.n_cols:
            raise ValueError("Not equal number of columns")

        matrix_mul = Matrix(
            [[0 for _ in range(self.n_cols)] for _ in range(self.n_rows)]
        )

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                matrix_mul.data[i][j] = self.data[i][j] * matrix.data[i][j]

        return matrix_mul

    def __matmul__(self, matrix):
        if self.n_cols != matrix.n_rows:
            raise ValueError("Incorrect matrix shape")

        matrix_matmul = Matrix(
            [[0 for _ in range(matrix.n_cols)] for _ in range(self.n_rows)]
        )

        for i in range(self.n_rows):
            for j in range(matrix.n_cols):
                matrix_matmul.data[i][j] = sum(
                    [self.data[i][k] * matrix.data[k][j] for k in range(self.n_cols)]
                )

        return matrix_matmul

    def __str__(self):
        return "\n".join(map(str, self.data))


if __name__ == "__main__":
    np.random.seed(0)

    a = Matrix(data=np.random.randint(0, 10, (10, 10)))

    b = Matrix(data=np.random.randint(0, 10, (10, 10)))

    with open("./artefacts/3.1/matrix+.txt", "w") as f:
        f.write(str(a + b))

    with open("./artefacts/3.1/matrix*.txt", "w") as f:
        f.write(str(a * b))

    with open("./artefacts/3.1/matrix@.txt", "w") as f:
        f.write(str(a @ b))
