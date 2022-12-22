import aocd
import numpy as np


class Tree:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        self.files = []
        self.parent = parent

    def path(self):
        loc = self
        p = self.name
        while loc.parent != None:
            p = loc.parent.name + "/" + p
            loc = loc.parent
        return p

    def add_child(self, name):
        for c in self.children:
            if c.name == name:
                return c
        t = Tree(name, self)
        self.children.append(t)
        return t

    def add_file(self, size, file):
        self.files.append([file, int(size)])

    def navigate(self):
        size = sum([f[1] for f in self.files])
        sizes = {}
        for c in self.children:
            sizes = {**sizes, **c.navigate()}
        size += sum([sizes[ch.path()] for ch in self.children])
        sizes[self.path()] = size
        return sizes


if __name__ == "__main__":

    input = aocd.get_data(day=7, year=2022)
    lines = input.split("\n")
    i = 1
    base = Tree("/")
    loc = base
    while i < len(lines):
        if lines[i] == "$ ls":
            while i + 1 < len(lines) and lines[i + 1][0] != "$":
                i += 1
                if lines[i][0:3] == "dir":
                    loc.add_child(lines[i].split(" ")[1])
                else:
                    loc.add_file(lines[i].split(" ")[0], lines[i].split(" ")[1])
        elif lines[i] == "$ cd ..":
            loc = loc.parent
        elif "$ cd " in lines[i]:
            loc = loc.add_child(lines[i].split(" ")[2])
        else:
            print("uncaptured: ", lines[i])
        i += 1

    navigation = base.navigate()
    sizes = np.array(sorted(navigation.values()))
    print("1: ", sum(sizes[sizes <= 100000]))

    print("2: ", sizes[sizes > max(sizes) - 40000000][0])

