from functools import cache


topographic_map = []
trailheads = set()
for i, line in enumerate(open("input.txt")):
    topographic_map.append([-1])
    for j, num in enumerate(line.strip()):
        topographic_map[i].append(int(num))
        if num == "0":
            trailheads |= {(j + 1, i + 1)}
    topographic_map[i].append(-1)


topographic_map = [[-1] * len(topographic_map[0])] + topographic_map + [[-1] * len(topographic_map[0])]
topographic_map = tuple(map(tuple, topographic_map))

# Part 1
@cache
def find_peak(curr_pos, topographic_map):
    x, y = curr_pos
    curr_num = topographic_map[y][x]
    if curr_num == 9:
        return {curr_pos}

    peaks = set()
    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):

        if curr_num + 1 == topographic_map[y + dy][x + dx]:
            peaks |= find_peak((x + dx, y + dy), topographic_map)

    return peaks


# Part 2
"""@cache
def path_count(x, y, topographic_map):
    curr_num = topographic_map[y][x]
    if curr_num == 9:
        return 1

    return sum(path_count(x + dx, y + dy, topographic_map) for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1))
               if curr_num + 1 == topographic_map[y + dy][x + dx])"""

# one-liner :)
@cache
def path_count(x, y, topographic_map):
    return topographic_map[y][x] == 9 or sum(path_count(x + dx, y + dy, topographic_map)
                                            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1))
                                            if topographic_map[y][x] + 1 == topographic_map[y + dy][x + dx])


res = 0
res2 = 0
for trailhead in trailheads:
    res += len(find_peak(trailhead, topographic_map))
    res2 += path_count(*trailhead, topographic_map)

print(res)
print(res2)
