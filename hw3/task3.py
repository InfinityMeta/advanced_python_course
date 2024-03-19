class HashMixin:
    def __hash__(self, m=9) -> int:
        """
        A - хэшируемая матрица с n строками и k столбцами, тогда:
        lu: остаток от деления на m элемента A в 1 строке и 1 столбце
        ru: остаток от деления на m элемента A в 1 строке и k столбце
        rd: остаток от деления на m элемента A в n строке и k столбце
        ld: остаток от деления на m элемента A в n строке и 1 столбце

        hash = 10000 + lu * 1000 + ru * 100 + rd * 10 + ld
        """
        lu = self.data[0][0] % m
        ru = self.data[0][self.n_cols - 1] % m
        rd = self.data[self.n_rows - 1][self.n_cols - 1] % m
        ld = self.data[self.n_rows - 1][0] % m
        hash = 1e4 + lu * 1e3 + ru * 1e2 + rd * 10 + ld
        return int(hash)

    def __eq__(self, matrix):
        if self.n_rows != matrix.n_rows:
            raise ValueError("Not equal number of rows")
        if self.n_cols != matrix.n_cols:
            raise ValueError("Not equal number of columns")

        for i in range(self.n_rows):
            if self.data[i] != matrix.data[i]:
                return False

        return True


class WriteToFileMixin:
    def write_to_file(self, file_path):
        with open(file_path, "w") as f:
            f.write(str(self))


class Matrix(HashMixin, WriteToFileMixin):

    cache = {}

    def __init__(self, data) -> None:
        self.data = data
        self.n_rows = len(data)
        self.n_cols = len(data[0])

    def __add__(self, matrix):
        if self.n_rows != matrix.n_rows:
            raise ValueError("Not equal number of rows")
        if self.n_cols != matrix.n_cols:
            raise ValueError("Not equal number of columns")

        sum_body = [[0 for _ in range(self.n_cols)] for _ in range(self.n_rows)]

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                sum_body[i][j] = self.data[i][j] + matrix.data[i][j]

        sum_body = tuple(map(tuple, sum_body))

        matrix_sum = Matrix(data=sum_body)

        return matrix_sum

    def __mul__(self, matrix):
        if self.n_rows != matrix.n_rows:
            raise ValueError("Not equal number of rows")
        if self.n_cols != matrix.n_cols:
            raise ValueError("Not equal number of columns")

        mul_body = [[0 for _ in range(self.n_cols)] for _ in range(self.n_rows)]

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                mul_body[i][j] = self.data[i][j] * matrix.data[i][j]

        mul_body = tuple(map(tuple, mul_body))

        matrix_mul = Matrix(data=mul_body)

        return matrix_mul

    def __matmul__(self, matrix):

        if (hash(self), hash(matrix)) in self.cache:
            return self.cache[(hash(self), hash(matrix))]

        if self.n_cols != matrix.n_rows:
            raise ValueError("Incorrect matrix shape")

        matmul_body = [[0 for _ in range(matrix.n_cols)] for _ in range(self.n_rows)]

        for i in range(self.n_rows):
            for j in range(matrix.n_cols):
                matmul_body[i][j] = sum(
                    (self.data[i][k] * matrix.data[k][j] for k in range(self.n_cols))
                )

        matmul_body = tuple(map(tuple, matmul_body))

        matrix_matmul = Matrix(data=matmul_body)

        self.cache[(hash(self), hash(matrix))] = matrix_matmul

        return matrix_matmul

    def __str__(self):
        return "\n".join(map(str, self.data))


if __name__ == "__main__":
    a = Matrix(data=((0, 1), (2, 3)))
    a.write_to_file("./artefacts/3.3/A.txt")

    c = Matrix(data=((9, 10), (11, 12)))
    c.write_to_file("./artefacts/3.3/C.txt")

    print(hash(a) == hash(c))  # True

    b = Matrix(data=((1, 2), (3, 4)))
    b.write_to_file("./artefacts/3.3/B.txt")

    d = Matrix(data=((1, 2), (3, 4)))
    d.write_to_file("./artefacts/3.3/D.txt")

    ab = a @ b
    ab.write_to_file("./artefacts/3.3/AB.txt")

    matmul_body = [[0 for _ in range(d.n_cols)] for _ in range(c.n_rows)]

    for i in range(c.n_rows):
        for j in range(d.n_cols):
            matmul_body[i][j] = sum(
                (c.data[i][k] * d.data[k][j] for k in range(c.n_cols))
            )

    matmul_body = tuple(map(tuple, matmul_body))

    cd = Matrix(data=matmul_body)
    cd.write_to_file("./artefacts/3.3/CD.txt")

    with open("./artefacts/3.3/hash.txt", "w") as f:
        f.write(f"AB hash: {hash(ab)} CD hash: {hash(cd)}")
