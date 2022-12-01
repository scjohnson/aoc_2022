import aocd

def max_cal(elves, num=1):
    cals = [sum(elf) for elf in elves]
    cals.sort(reverse=True)
    return sum(cals[0:num])


if __name__ == "__main__":

    input = aocd.get_data(day=1, year=2022)

    elves = [[int(x) for x in sub.split("\n")] for sub in input.split("\n\n")]

    print(max_cal(elves))
    print(max_cal(elves, 3))
