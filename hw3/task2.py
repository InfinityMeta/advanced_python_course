from numbers import Number
import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class GetterSetterMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data


class StrMixin:
    def __str__(self):
        return "\n".join(map(str, self.data))


class WriteToFileMixin:
    def write_to_file(self, file_path):
        with open(file_path, "w") as f:
            f.write(str(self))


custom_mixins = [GetterSetterMixin, StrMixin, WriteToFileMixin]


class Matrix(NDArrayOperatorsMixin, *custom_mixins):

    def __init__(self, data) -> None:
        self._data = data

    def __array_ufunc__(self, ufunc, method, *args, **kwargs):
        if method == "__call__":
            scalars = []
            for arg in args:
                if isinstance(arg, Number):
                    scalars.append(arg)
                elif isinstance(arg, self.__class__):
                    scalars.append(arg.data)
                else:
                    return NotImplemented
            return self.__class__(ufunc(*scalars, **kwargs))
        return NotImplemented


if __name__ == "__main__":
    np.random.seed(0)

    a = Matrix(data=np.random.randint(0, 10, (10, 10)))

    b = Matrix(data=np.random.randint(0, 10, (10, 10)))

    (a + b).write_to_file("./artefacts/3.2/matrix+.txt")

    (a * b).write_to_file("./artefacts/3.2/matrix*.txt")

    (a @ b).write_to_file("./artefacts/3.2/matrix@.txt")
