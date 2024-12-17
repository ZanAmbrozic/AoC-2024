from collections import defaultdict

start = None
end = None
tiles = set()


for i, line in enumerate(open("test.txt")):
    for j, char in enumerate(line.strip()):
        match char:
            case ".":
                tiles |= {(j, i)}
            case "S":
                start = (j, i)
                tiles |= {(j, i)}
            case "E":
                end = (j, i)
                tiles |= {(j, i)}


def sum_tuple(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


def get_f_score(curr, score, end):
    return score + get_heuristics(curr, end)

def get_heuristics(curr, end):
    return abs(curr[0] - end[0]) + abs(curr[1] - end[1])


# 0 - North, 1 - East, 2 - South, 3 - West
directions = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
steps = {(*start, 1): 0}
current = (*start, 1)


visited = set()

while current[:2] != end:
    moves = {(*pos, (current[2] + i) % 4) for i in range(-1, 2)
             if (pos := sum_tuple(directions[(current[2] + i) % 4], current[:2])) in tiles}

    for move in moves:
        if move[:2] in visited:
            continue
        price = (current[2] != move[2]) * 1000 + 1

        steps[move] = min(steps.get(move, steps[current] + price), steps[current] + price)

    visited |= {current[:2]}

    del steps[current]

    current = min(steps, key=lambda e: get_f_score(e, steps[e], end))


    #print(steps[current])
    #print(len(steps))


min_steps = steps[current]
print(min_steps)
