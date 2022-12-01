import aocd


if __name__ == "__main__":

    input = aocd.get_data(day=1, year=2022)

    elves = [[int(x) for x in sub.split("\n")] for sub in input.split("\n\n")]
    cals = [sum(elf) for elf in elves]
    cals.sort(reverse=True)
    print(cals[0])
    print(sum(cals[0:3]))

