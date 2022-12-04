import aocd


def overlap(first, second):
    if second[0] <= first[0] <= second[1]:
        return True
    elif second[0] <= first[1] <= second[1]:
        return True
    elif first[0] <= second[1] <= first[1]:
        return True
    elif first[0] <= second[1] <= first[1]:
        return True
    return False


def contains(first, second):
    if first[0] >= second[0] and first[1] <= second[1]:
        return True
    elif second[0] >= first[0] and second[1] <= first[1]:
        return True
    return False


if __name__ == "__main__":

    input = aocd.get_data(day=4, year=2022)
    num1 = 0
    num2 = 0
    for elem in input.split("\n"):
        first = [int(i) for i in elem.split(",")[0].split("-")]
        second = [int(i) for i in elem.split(",")[1].split("-")]
        if contains(first, second):
            num1 += 1
        if overlap(first, second):
            num2 += 1
    print(num1, num2)
