import aocd
import numpy as np

dirs = {
    "R": np.array([1, 0]),
    "U": np.array([0, 1]),
    "L": np.array([-1, 0]),
    "D": np.array([0, -1]),
}


def propagate_tails(head, tail):
    if abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2:
        return
    elif abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 2:
        tail[0] += (head[0] - tail[0]) // 2
        tail[1] += (head[1] - tail[1]) // 2
    elif abs(head[0] - tail[0]) == 0:
        tail[1] += (head[1] - tail[1]) // 2
    elif abs(head[1] - tail[1]) == 0:
        tail[0] += (head[0] - tail[0]) // 2
    elif abs(head[0] - tail[0]) == 2:
        tail[1] += head[1] - tail[1]
        tail[0] += (head[0] - tail[0]) // 2
    elif abs(head[1] - tail[1]) == 2:
        tail[0] += head[0] - tail[0]
        tail[1] += (head[1] - tail[1]) // 2
    else:
        print("uncaptured tail move: ", head, tail)


class Rope:
    def __init__(self, num_knots=2):
        self.knots = []
        for i in range(num_knots):
            self.knots.append(np.array([0, 0]))
        self.locs = {}
        self.visited = []

    def move(self, dir):
        self.knots[0] += dirs[dir]
        for i in range(len(self.knots) - 1):
            propagate_tails(self.knots[i], self.knots[i + 1])
        self.visited.append(str(self.knots[-1][0]) + " " + str(self.knots[-1][1]))


if __name__ == "__main__":

    input = aocd.get_data(day=9, year=2022)

    rope2 = Rope(2)
    rope10 = Rope(10)

    for move in input.split("\n"):
        direction, number = move.split(" ")
        for n in range(int(number)):
            rope2.move(direction)
            rope10.move(direction)
    print(len(set(rope2.visited)))
    print(len(set(rope10.visited)))
