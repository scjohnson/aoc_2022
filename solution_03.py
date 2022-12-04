import aocd


def calc_score(letter):
    if letter.islower():
        return ord(letter) - ord("a") + 1
    else:
        return ord(letter) - ord("A") + 27


def doubled(rucksack):
    half = int(len(rucksack) / 2)
    for i in rucksack[0 : half + 1]:
        if i in rucksack[half:]:
            return i
    return None


def tripled(rs1, rs2, rs3):
    for i in rs1:
        if i in rs2 and i in rs3:
            return i
    return None


if __name__ == "__main__":

    input = aocd.get_data(day=3, year=2022)

    score = 0
    for rs in input.split("\n"):
        score += calc_score(doubled(rs))

    print(score)

    score = 0
    rss = input.split("\n")
    for i in range(int(len(rss) / 3)):
        score += calc_score(tripled(rss[i * 3], rss[i * 3 + 1], rss[i * 3 + 2]))
    print(score)
