import aocd
import numpy as np
import matplotlib.pyplot as pyplot
import operator


def left(loc):
    return tuple(map(operator.add, loc, (-1, 1)))


def right(loc):
    return tuple(map(operator.add, loc, (1, 1)))


def down(loc):
    return tuple(map(operator.add, loc, (0, 1)))


def drop_sand(space):
    loc = (500, 0)
    if space[loc] == 2:
        return False

    while True:
        if loc[1] == 549:
            return False

        if space[down(loc)] == 0:
            loc = down(loc)
        elif space[left(loc)] == 0:
            loc = left(loc)
        elif space[right(loc)] == 0:
            loc = right(loc)
        else:
            space[loc] = 2
            return True


if __name__ == "__main__":

    input = aocd.get_data(day=14, year=2022)
    #input = "498,4 -> 498,6 -> 496,6\n503,4 -> 502,4 -> 502,9 -> 494,9"
    space = np.zeros((1000, 1000), dtype=int)
    maxy = 0
    for line in input.split("\n"):
        points = line.split(" -> ")
        for i in range(len(points) - 1):
            x1, y1 = [int(x) for x in points[i].split(",")]
            x2, y2 = [int(x) for x in points[i + 1].split(",")]
            x1, x2 = min([x1, x2]), max([x1, x2])
            y1, y2 = min([y1, y2]), max([y1, y2])
            maxy = max([maxy, y1, y2])
            space[x1 : x2 + 1, y1 : y2 + 1] = 1
    
    floor_space = np.copy(space)
    floor_space[:,maxy + 2] = 1
    sands = 0
    while drop_sand(space):
        sands += 1
    print(sands)  # 873
    sands = 0
    while drop_sand(floor_space):
        sands += 1
    print(sands)  # 873
    
    #pyplot.imshow(space)
    #pyplot.show()
    # 29044
