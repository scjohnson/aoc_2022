import aocd
from collections import deque
import numpy as np

if __name__ == "__main__":

    input = aocd.get_data(day=12, year=2022)
    # input = "Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi"
    lines = input.split("\n")
    ar = np.array([[c for c in line] for line in lines])

    popper = deque()

    distances = -1 * np.ones(ar.shape, dtype="int")
    start = (np.where(ar == "S")[0][0], np.where(ar == "S")[1][0])
    end = (np.where(ar == "E")[0][0], np.where(ar == "E")[1][0])
    ar[start] = "a"
    ar[end] = "z"

    distances[end] = 0
    popper.append((end, 0))

    while popper:
        (x, y), distance = popper.popleft()
        distance += 1

        for delx, dely in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newx, newy = x + delx, y + dely

            if (
                0 <= newx < ar.shape[0]
                and 0 <= newy < ar.shape[1]
                and distances[(newx, newy)] == -1
                and ord(ar[x][y]) - ord(ar[newx][newy]) <= 1
            ):
                distances[(newx, newy)] = distance
                popper.append(((newx, newy), distance))
    print(distances[start])  # 420
    print(sorted(distances[(ar == "a") & (distances != -1)])[0])  # 416 too high

