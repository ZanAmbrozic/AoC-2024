walls = set()
boxes = set()
robot = None

wide_walls = set()
wide_boxes = set()
wide_robot = None
double_boxes = {}

directions = {"<": (-1, 0), ">": (1, 0), "v": (0, 1), "^": (0, -1)}


def sum_pos(t1, t2):
    return tuple(e1 + e2 for e1, e2 in zip(t1, t2))


def attempt_move(old_box_pos, direction, walls, boxes, directions):
    new_box_pos = sum_pos(old_box_pos, directions[direction])
    if new_box_pos in walls:
        return False
    if new_box_pos in boxes and not attempt_move(new_box_pos, direction, walls, boxes, directions):
        return False
    boxes.remove(old_box_pos)
    boxes.add(new_box_pos)
    return True


def attempt_move_double(robot_pos, direction, walls, boxes, directions):
    to_move = [robot_pos]

    for obj_pos in to_move:
        new_obj_pos = sum_pos(obj_pos, directions[direction])

        if new_obj_pos in walls:
            return robot_pos

        if new_obj_pos in to_move:
            continue

        if obj_pos in boxes:
            if boxes[obj_pos] is True:
                if sum_pos(obj_pos, (1, 0)) not in to_move:
                    to_move.append(sum_pos(obj_pos, (1, 0)))
            else:
                if sum_pos(obj_pos, (-1, 0)) not in to_move:
                    to_move.append(sum_pos(obj_pos, (-1, 0)))

        if new_obj_pos in boxes and new_obj_pos not in to_move:
            to_move.append(new_obj_pos)

    for obj_pos in to_move[::-1]:
        new_obj_pos = sum_pos(obj_pos, directions[direction])
        if obj_pos not in boxes:
            return new_obj_pos

        boxes[new_obj_pos] = boxes[obj_pos]
        del boxes[obj_pos]



for i, line in enumerate(open("input.txt")):
    line = line.strip()

    for j, char in enumerate(line):
        match char:
            case "#":
                walls |= {(j, i)}
                wide_walls |= {(2 * j, i), (2 * j + 1, i)}
            case "O":
                boxes |= {(j, i)}
                wide_boxes |= {(2 * j, i)}
                double_boxes[(2 * j, i)] = True
                double_boxes[2 * j + 1, i] = False
            case "@":
                robot = (j, i)
                wide_robot = (2 * j, i)
            case "<" | ">" | "v" | "^":
                # Part 1
                """new_pos = sum_pos(robot, directions[char])
                if new_pos in walls:
                    continue
                if new_pos in boxes:
                    can_move = attempt_move(new_pos, char, walls, boxes, directions)
                    robot = new_pos if can_move else robot
                    continue
                robot = new_pos"""

                # Part 2
                wide_robot = attempt_move_double(wide_robot, char, wide_walls, double_boxes, directions)

res = 0
for x, y in boxes:
    res += 100 * y + x

res2 = 0
for (x, y), is_left in double_boxes.items():
    if not is_left:
        continue
    res2 += 100 * y + x

print(res)
print(res2)




