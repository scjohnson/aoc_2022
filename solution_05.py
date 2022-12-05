import aocd
import copy


if __name__ == "__main__":

    input = aocd.get_data(day=5, year=2022)
    initial, moves = input.split("\n\n")

    num_stacks = (len(initial.split("\n")[0])+1)//4
    stacks = [[] for i in range(num_stacks)]
    for ini in initial.split("\n"):
        for i in range(num_stacks):
            if ini[i*4+1] != ' ':
                stacks[i].append(ini[i*4+1])

    for stack in stacks:
        stack.reverse()

    stacks2 = copy.deepcopy(stacks)

    for move in moves.split("\n"):
        _, num, _, fro, _, to = move.split(" ")
        num, fro, to = int(num), int(fro), int(to)
        for n in range(num):
            stacks[to-1].append(stacks[fro-1].pop())
        stacks2[to-1].extend(stacks2[fro-1][-num:])
        stacks2[fro-1] = stacks2[fro-1][0:-num]

    print("".join([stack[-1] for stack in stacks]))
    print("".join([stack2[-1] for stack2 in stacks2]))