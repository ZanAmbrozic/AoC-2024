from collections import defaultdict
import re

def move_hundred_times(curr_x, curr_y, curr_vel_x, curr_vel_y, max_w, max_h):
    pos_x = (100 * curr_vel_x + curr_x) % max_w
    pos_y = (100 * curr_vel_y + curr_y) % max_h

    return pos_x, pos_y


def move_n_times(n, curr_x, curr_y, curr_vel_x, curr_vel_y, max_w, max_h):
    pos_x = (n * curr_vel_x + curr_x) % max_w
    pos_y = (n * curr_vel_y + curr_y) % max_h

    return pos_x, pos_y


positions = defaultdict(int)
# max_pos = (11, 7)
max_pos = (101, 103)

start_pos = []

for line in open("input.txt"):
    x, y, v_x, v_y = re.findall(r"-?[0-9]+", line)

    start_pos.append((int(x), int(y), int(v_x), int(v_y)))

    pos_x, pos_y = move_hundred_times(int(x), int(y), int(v_x), int(v_y), *max_pos)

    positions[(pos_x, pos_y)] += 1


res = 1
res *= sum(val for (x, y), val in positions.items() if x < (max_pos[0] - 1) // 2 and y < (max_pos[1] - 1) // 2)
res *= sum(val for (x, y), val in positions.items() if x < (max_pos[0] - 1) // 2 and y > (max_pos[1] - 1) // 2)
res *= sum(val for (x, y), val in positions.items() if x > (max_pos[0] - 1) // 2 and y < (max_pos[1] - 1) // 2)
res *= sum(val for (x, y), val in positions.items() if x > (max_pos[0] - 1) // 2 and y > (max_pos[1] - 1) // 2)

print(res)


min_i = None
min_val = None
for i in range(0, 15000):
    positions = defaultdict(int)
    for x, y, v_x, v_y in start_pos:
        pos_x, pos_y = move_n_times(i, x, y, v_x, v_y, *max_pos)

        positions[(pos_x, pos_y)] += 1

    test_val = 1
    test_val *= sum(val for (x, y), val in positions.items() if x < (max_pos[0] - 1) // 2 and y < (max_pos[1] - 1) // 2)
    test_val *= sum(val for (x, y), val in positions.items() if x < (max_pos[0] - 1) // 2 and y > (max_pos[1] - 1) // 2)
    test_val *= sum(val for (x, y), val in positions.items() if x > (max_pos[0] - 1) // 2 and y < (max_pos[1] - 1) // 2)
    test_val *= sum(val for (x, y), val in positions.items() if x > (max_pos[0] - 1) // 2 and y > (max_pos[1] - 1) // 2)

    if min_val is None or test_val < min_val:
        min_val = test_val
        min_i = i

print(min_i)

