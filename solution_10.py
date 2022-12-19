import aocd
import functools
import operator


class CPU:
    def __init__(self):
        self.x = 1
        self.cycles = 0
        self.history = {}
        self.screen = ""

    def cycle(self):
        cycles_of_interest = [20, 60, 100, 140, 180, 220]
        if abs(self.cycles % 40 - self.x) < 2:
            self.screen += "#"
        else:
            self.screen += "."
        self.cycles += 1
        if self.cycles in cycles_of_interest:
            self.history[self.cycles] = self.x

    def run(self, command):
        if command == "noop":
            self.cycle()
        else:
            self.cycle()
            self.cycle()
            self.x += int(command.split(" ")[1])


if __name__ == "__main__":

    input = aocd.get_data(day=10, year=2022)
    cpu = CPU()

    for command in input.split("\n"):
        cpu.run(command)

    score = 0
    for k, v in cpu.history.items():
        score += k * v
    print(score)

    for i in range(0, 240, 40):
        print(cpu.screen[i : i + 40])

