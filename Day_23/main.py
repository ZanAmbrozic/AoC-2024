from collections import defaultdict
from itertools import combinations

connections = defaultdict(set)

for line in open("input.txt"):
    c1, c2 = line.strip().split("-")

    connections[c1] |= {c2}
    connections[c2] |= {c1}


# Part 1
res = set()
for node, conns in connections.items():
    if node[0] != "t":
        continue

    for c1, c2 in combinations(conns, 2):
        if c1 in connections[c2] and c2 in connections[c1]:
            res |= {tuple(sorted((node, c1, c2)))}

print(len(res))


# Part 2
def bron_kerbosch_algo(r, p, x):
    if not p and not x:
        return r

    longest = frozenset()
    for vertex in p:
        longest = max([bron_kerbosch_algo(r | {vertex}, p & connections[vertex], x & connections[vertex]), longest], key=lambda e: len(e))
        p = p - {vertex}
        x = x | {vertex}
    return longest


# did it with frozensets because I thought it would require caching
res = bron_kerbosch_algo(frozenset(), frozenset(connections), frozenset())

print(",".join(sorted(res)))
