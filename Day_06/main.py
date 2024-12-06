# solution is not the best

obstacles = set()
visited = set()
curr_pos = None
curr_dir = None
max_coor = None
start_pos = None

directions = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}  # up, right, down, left

for i, line in enumerate(open("input.txt")):
    line = line.strip()

    obstacles |= {(j, i) for j, char in enumerate(line) if char == "#"}
    max_coor = (len(line) - 1, i)

    if "^" in line:
        curr_pos = [(line.find("^"), i), 0]
        start_pos = curr_pos.copy()


def sum_tuple(t1, t2):
    return tuple(e1 + e2 for e1, e2 in zip(t1, t2))


# part 1
while 0 <= curr_pos[0][0] <= max_coor[0] and 0 <= curr_pos[0][1] <= max_coor[1]:
    visited |= {curr_pos[0]}
    if (x:= sum_tuple(curr_pos[0], directions[curr_pos[1]])) not in obstacles:
        curr_pos[0] = x
    else:
        curr_pos[1] = (curr_pos[1] + 1) % len(directions)

print(len(visited))


# part 2

def loop_check(start_pos, obstacles):
    visited = set()
    curr_pos = start_pos.copy()

    while 0 <= curr_pos[0][0] <= max_coor[0] and 0 <= curr_pos[0][1] <= max_coor[1]:
        if tuple(curr_pos) in visited:
            return 1

        visited |= {tuple(curr_pos)}
        if (x := sum_tuple(curr_pos[0], directions[curr_pos[1]])) not in obstacles:
            curr_pos[0] = x
        else:
            curr_pos[1] = (curr_pos[1] + 1) % len(directions)

    return 0


res = 0

res = sum(loop_check(start_pos, obstacles | {pos}) for pos in visited)

print(res)













