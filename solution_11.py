import aocd
import functools
import operator


class Monkey:
    def __init__(self, m):
        lines = m.split("\n")
        li = lines[1].split(":")[1]
        self.items = [int(l) for l in li.split(",")]
        self.operation = lines[2].split("= ")[1]
        self.divisible = int(lines[3].split(" ")[-1])
        self.if_true = int(lines[4].split(" ")[-1])
        self.if_false = int(lines[5].split(" ")[-1])
        self.num = 0

    def process(self, monkeys, factor=None):
        for old in self.items:
            self.num += 1
            new = eval(self.operation)
            if factor:
                new = new % factor
            else:
                new = new // 3
            if new % self.divisible == 0:
                monkeys[self.if_true].items.append(new)
            else:
                monkeys[self.if_false].items.append(new)
        self.items = []


if __name__ == "__main__":

    input = aocd.get_data(day=11, year=2022)

    monkeys = [Monkey(i) for i in input.split("\n\n")]
    for _ in range(20):
        for monkey in monkeys:
            throws = monkey.process(monkeys)
    scores = sorted([m.num for m in monkeys])
    print(scores[-1] * scores[-2])

    monkeys = [Monkey(i) for i in input.split("\n\n")]
    factor = functools.reduce(operator.mul, [m.divisible for m in monkeys])
    for _ in range(10000):
        for monkey in monkeys:
            throws = monkey.process(monkeys, factor)
    scores = sorted([m.num for m in monkeys])
    print(scores[-1] * scores[-2])
