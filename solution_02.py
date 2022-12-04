import aocd

scores = {"X": 1, "Y": 2, "Z": 3}
scores2 = {"X": 0, "Y": 3, "Z": 6}


def calc_score2(hand1, hand2):
    score = 0
    if hand1 == "A":
        if hand2 == "X":
            score = 3
        elif hand2 == "Y":
            score = 1
        else:
            score = 2
    elif hand1 == "B":
        if hand2 == "X":
            score = 1
        elif hand2 == "Y":
            score = 2
        else:
            score = 3
    elif hand1 == "C":
        if hand2 == "X":
            score = 2
        elif hand2 == "Y":
            score = 3
        else:
            score = 1
    score += scores2[hand2]
    return score


def calc_score(hand1, hand2):
    score = 0
    if hand1 == "A":
        if hand2 == "X":
            score = 3
        elif hand2 == "Y":
            score = 6
        else:
            score = 0
    elif hand1 == "B":
        if hand2 == "X":
            score = 0
        elif hand2 == "Y":
            score = 3
        else:
            score = 6
    elif hand1 == "C":
        if hand2 == "X":
            score = 6
        elif hand2 == "Y":
            score = 0
        else:
            score = 3
    score += scores[hand2]
    return score


if __name__ == "__main__":

    input = aocd.get_data(day=2, year=2022)
    score = 0
    score2 = 0
    for line in input.split("\n"):
        hands = line.split(" ")
        print(hands)
        score += calc_score(hands[0], hands[1])
        score2 += calc_score2(hands[0], hands[1])
    print(score)
    print(score2)  # too low 10322

