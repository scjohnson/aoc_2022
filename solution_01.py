def max_cal(elves, num=1):
    cals = [sum(elf) for elf in elves]
    cals.sort(reverse=True)
    return sum(cals[0:num])


if __name__ == "__main__":

    with open("input_01.txt", "r") as file:
        input = file.read().split("\n\n")

        elves = [[int(x) for x in sub.split("\n")] for sub in input]

        print(max_cal(elves))
        print(max_cal(elves, 3))
