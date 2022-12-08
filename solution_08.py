import aocd
import numpy as np
import itertools
import functools
import operator


def viewable(a, i, j):
    height = a[i, j]
    a -= height
    if np.all(a[i, 0:j] < 0):
        return True
    elif np.all(a[i, j + 1 :] < 0):
        return True
    elif np.all(a[0:i, j] < 0):
        return True
    elif np.all(a[i + 1 :, j] < 0):
        return True
    return False


def line_score(b, height):
    for i in range(len(b)):
        if b[i] >= height:
            return i + 1
    return len(b)


def scenic_score(a, i, j):
    lengths = []
    lengths.append(line_score(np.flip(a[i, 0:j]), a[i, j]))
    lengths.append(line_score(a[i, j + 1 :], a[i, j]))
    lengths.append(line_score(np.flip(a[0:i, j]), a[i, j]))
    lengths.append(line_score(a[i + 1 :, j], a[i, j]))
    return functools.reduce(operator.mul, lengths, 1)

if __name__ == "__main__":

    input = aocd.get_data(day=8, year=2022)
    a = np.array([[int(n) for n in line] for line in input.split("\n")])

    print(
        sum(
            [
                viewable(a, i, j)
                for i, j in itertools.product(range(a.shape[0]), range(a.shape[1]))
            ]
        )
    )

    print(
        max(
            [
                scenic_score(a, i, j)
                for i, j in itertools.product(range(a.shape[0]), range(a.shape[1]))
            ]
        )
    )

