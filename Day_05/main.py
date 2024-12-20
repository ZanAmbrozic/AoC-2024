from collections import defaultdict

conditions = defaultdict(set)
adding = True

res = 0
res2 = 0
for line in open("input.txt"):
    line = line.strip()
    if line == "":
        adding = False
        continue
    if adding is True:
        v, k = line.split("|")
        conditions[k] |= {v}
        continue

    updates = line.split(",")
    used = set()

    for update in updates:
        # check if used is a subset of required updates
        # if it is, it means that requirements are not met and updates are not in order
        # part 1 only needs break in if statement body
        if used < (conditions[update] & set(updates)):
            ordered = sorted(updates, key=lambda e: len(set(updates) & conditions[e]))
            res2 += int(ordered[len(ordered) // 2])
            break

        used |= {update}

    else:
        res += int(updates[len(updates) // 2])

print(res)
print(res2)


