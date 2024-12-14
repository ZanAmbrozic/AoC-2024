from itertools import pairwise

plots = []
for i, line in enumerate(open("input.txt")):
    line = line.strip()
    plots.append(["."] + list(line) + ["."])

plots = [["."] * len(plots[0])] + plots + [["."] * len(plots[0])]


def area_and_border_and_corner_count(x, y, plots):
    plot = plots[y][x]

    area = 0
    border = 0
    corners = set()

    if plot == "." or plot.islower():
        return 0, 0, 0

    a1, a2, a3 = plots[y - 1][x - 1], plots[y - 1][x], plots[y - 1][x + 1]
    a4,     a6 = plots[y][x - 1], plots[y][x + 1]
    a7, a8, a9 = plots[y + 1][x - 1], plots[y + 1][x], plots[y + 1][x + 1]


    if (a4 + a1 + a2).lower().count(plot.lower()) % 2 == 0:
        corners |= {(x - 0.5, y - 0.5)}

    if (a2 + a3 + a6).lower().count(plot.lower()) % 2 == 0:
        corners |= {(x + 0.5, y - 0.5)}

    if (a6 + a9 + a8).lower().count(plot.lower()) % 2 == 0:
        corners |= {(x + 0.5, y + 0.5)}

    if (a8 + a7 + a4).lower().count(plot.lower()) % 2 == 0:
        corners |= {(x - 0.5, y + 0.5)}

    # only in case there is a diagonal, because it would only count the corner once
    if (plot.lower() not in (a4 + a2).lower() and plot.lower() == a1.lower() or
            plot.lower() not in (a2 + a6).lower() and plot.lower() == a3.lower() or
            plot.lower() not in (a6 + a8).lower() and plot.lower() == a9.lower() or
            plot.lower() not in (a8 + a4).lower() and plot.lower() == a7.lower()):
        corners |= {(x + 0.1, y + 0.1)}

    plots[y][x] = plot.lower()
    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        if plots[y + dy][x + dx] == plot:
            a, b, c = area_and_border_and_corner_count(x + dx, y + dy, plots)
            area += a
            border += b
            corners |= c
            continue

        if plots[y + dy][x + dx] != plot.lower():
            border += 1

    return area + 1, border, corners



res = 0
res2 = 0
for i, line in enumerate(plots):
    for j, (curr, nxt) in enumerate(pairwise(line)):
        if curr == nxt:
            continue
        if curr == "." or curr.islower():
            continue

        a, b, c = area_and_border_and_corner_count(j, i, plots)
        res += a * b
        res2 += a * len(c)

print(res)
print(res2)