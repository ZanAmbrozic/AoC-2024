import math
from collections import OrderedDict

path = set()
walls = set()
start = None
end = None


for i, line in enumerate(open("input.txt")):
    for j, char in enumerate(line.strip()):
        match char:
            case ".":
                path |= {(j, i)}
            case "S":
                start = (j, i)
                path |= {(j, i)}
            case "E":
                end = (j, i)
                path |= {(j, i)}
            case "#":
                walls |= {j, i}


def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def sum_tuple(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


prev = None
current = start
visited = OrderedDict({start: 0})
cost = 0


while current != end:
    move = next(sum_tuple(pos, current) for pos in ((-1, 0), (0, -1), (1, 0), (0, 1))
                if sum_tuple(pos, current) in path and sum_tuple(pos, current) != prev)
    cost += 1
    visited[move] = cost
    prev, current = current, move



res = 0
res2 = set()
for node, dist in visited.items():
    for node2, dist2 in visited.items():
        # Part 1
        if manhattan_dist(node, node2) <= 2 and dist - dist2 - manhattan_dist(node, node2) >= 100:
            res += 1

        # Part 2
        if manhattan_dist(node, node2) <= 20 and dist2 - dist - manhattan_dist(node, node2) >= 100:
            res2 |= {(node, node2)}

print(res)
print(len(res2))
