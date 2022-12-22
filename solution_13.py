import aocd
from functools import cmp_to_key


def compare(first, second):
    for i, j in zip(first, second):
        if type(i) == int and type(j) == list:
            res = compare([i], j)
            if res != None:
                return res
        elif type(i) == list and type(j) == int:
            res = compare(i, [j])
            if res != None:
                return res
        elif type(i) == list and type(j) == list:
            res = compare(i, j)
            if res != None:
                return res
        elif i < j:
            return 1
        elif i > j:
            return -1
    if len(first) < len(second):
        return 1
    elif len(second) < len(first):
        return -1
    return None


if __name__ == "__main__":

    input = aocd.get_data(day=13, year=2022)
    # input = "[1,1,3,1,1]\n[1,1,5,1,1]\n\n[[1],[2,3,4]]\n[[1],4]\n\n[9]\n[[8,7,6]]\n\n[[4,4],4,4]\n[[4,4],4,4,4]\n\n[7,7,7,7]\n[7,7,7]\n\n[]\n[3]\n\n[[[]]]\n[[]]\n\n[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]"
    score = 0
    all_packets = []
    for i, pairs in enumerate(input.split("\n\n")):
        first, second = pairs.split("\n")
        if compare(eval(first), eval(second)) != -1:
            score += i + 1
        all_packets.append(eval(first))
        all_packets.append(eval(second))
    print(score)
    all_packets.append(eval("[[2]]"))
    all_packets.append(eval("[[6]]"))
    all_packets.sort(key=cmp_to_key(compare), reverse=True)
    print(
        (all_packets.index(eval("[[2]]")) + 1) * (all_packets.index(eval("[[6]]")) + 1)
    )

