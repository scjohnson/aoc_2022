import aocd

def value(input, v):
    i = 0
    while len(set(input[i:i+v])) < v:
        i += 1
    return i+v

if __name__ == "__main__":

    input = aocd.get_data(day=6, year=2022)

    print(value(input, 4))
    print(value(input, 14))
