from collections import defaultdict
from itertools import combinations

nodes = defaultdict(list)
max_coor = (0, 0)
for i, line in enumerate(open("input.txt")):
    for j, char in enumerate(line.strip()):
        max_coor = (j, i)
        if char == ".":
            continue

        nodes[char].append((j, i))


# Part 1

antinodes = set()
for node_type, coors in nodes.items():
    for (x1, y1), (x2, y2) in combinations(coors, 2):
        dx, dy = x2 - x1, y2 - y1

        antinodes |= {(x1 - dx, y1 - dy), (x2 + dx, y2 + dy)}

antinodes = set(filter(lambda e: 0 <= e[0] <= max_coor[0] and 0 <= e[1] <= max_coor[1], antinodes))

print(len(antinodes))


# Part 2

antinodes = set()
for node_type, coors in nodes.items():
    for (x1, y1), (x2, y2) in combinations(coors, 2):
        dx, dy = x2 - x1, y2 - y1

        for k in range(-max_coor[0], max_coor[0]):
            antinodes |= {(x1 - k * dx, y1 - k * dy), (x2 + k * dx, y2 + k * dy)}

antinodes = set(filter(lambda e: 0 <= e[0] <= max_coor[0] and 0 <= e[1] <= max_coor[1], antinodes))

print(len(antinodes))


