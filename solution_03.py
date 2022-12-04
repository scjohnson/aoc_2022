import aocd
import itertools

def calc_score(letter):
    if letter.islower():
        return ord(letter) - ord("a") + 1
    else:
        return ord(letter) - ord("A") + 27


def doubled(rucksack):
    half = len(rucksack) // 2
    return list(set.intersection(set(rucksack[0:half]), set(rucksack[half:])))[0]


def tripled(rs1, rs2, rs3):
    return list(set.intersection(set(rs1), set(rs2), set(rs3)))[0]


if __name__ == "__main__":

    input = aocd.get_data(day=3, year=2022)

    scores = [calc_score(doubled(rs)) for rs in input.split("\n")]
    print(sum(scores))

    score = 0
    rss = input.split("\n")
    for i in range(len(rss) // 3):
        score += calc_score(tripled(rss[i * 3], rss[i * 3 + 1], rss[i * 3 + 2]))
    print(score)
