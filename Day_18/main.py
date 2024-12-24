from functools import cache

start = (0, 0)
number_of_fallen = 12
number_of_fallen = 1024
end = (6, 6)
end = (70, 70)

walls = []
for i, line in enumerate(open("input.txt")):
    x, y = line.strip().split(",")
    walls.append((int(x), int(y)))


@cache
def pathfinder(reps, prev_pos, pos, goal, walls):
    if pos == goal:
        return 1
    if reps <= 0:
        return 0

    res = 0
    for vx, vy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        dx, dy = pos[0] + vx, pos[1] + vy
        if not (0 <= dx <= goal[0]) or not (0 <= dy <= goal[1]):
            continue
        if (dx, dy) in walls:
            continue
        if (dx, dy) == prev_pos:
            continue

        if x := pathfinder(reps - 1, pos, (dx, dy), goal, walls):
            return x + 1

    return res


def bfs(start, goal, walls):
    current = start
    visited = {current}
    queue = []

    while current != end:
        visited |= {current}
        for vx, vy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dx, dy = current[0] + vx, current[1] + vy
            if (dx, dy) in visited or (dx, dy) in queue:
                continue
            if (dx, dy) in walls:
                continue
            if not (0 <= dx <= goal[0]) or not (0 <= dy <= goal[1]):
                continue

            queue = [(dx, dy)] + queue

        if not queue:
            return False

        current = queue.pop()
    return True


# Part 1
reps = abs(end[0] - start[0]) + abs(end[1] - start[1])
limited_walls = tuple(walls[:number_of_fallen])
while not (res := pathfinder(reps, (-1, -1), start, end, limited_walls)):
    reps += 1

print(res - 1)

# Part 2
num_of_walls = len(walls) - 1
while not bfs(start, end, walls[:num_of_walls]):
    num_of_walls -= 1
print(walls[num_of_walls])


