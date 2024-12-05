from itertools import pairwise


# part 1
res = 0
for line in open("input.txt"):
    seq = line.split()
    decreasing = None
    for p, n in pairwise(seq):
        diff = int(n) - int(p)
        if decreasing is None:
            decreasing = diff < 0
        if not (0 < abs(diff) < 4) or (decreasing is True and diff > 0) or (decreasing is False and diff < 0):
            break
    else:
        res += 1

print(res)


# part 2
res = 0
for line in open("input.txt"):
    seq = line.split()

    for i in range(0, len(seq)):
        tester = seq.copy()
        del tester[i]

        decreasing = None
        for p, n in pairwise(tester):
            diff = int(n) - int(p)
            if decreasing is None:
                decreasing = diff < 0
            if not (0 < abs(diff) < 4) or (decreasing is True and diff > 0) or (decreasing is False and diff < 0):
                break
        else:
            res += 1
            break

print(res)


