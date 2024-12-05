conditions = {}
adding = True

res = 0
res2 = 0
for line in open("input.txt"):
    if line.strip() == "":
        adding = False
        continue
    if adding is True:
        v, k = line.strip().split("|")
        conditions[k] = conditions.get(k, set()) | {v}
        continue

    updates = line.strip().split(",")
    used = set()

    for update in updates:
        if used < (conditions.get(update, set()) & set(updates)):
            ordered = sorted(updates, key=lambda e: len(set(updates) & conditions.get(e, set())))
            res2 += int(ordered[len(ordered) // 2])
            break
        used |= {update}

    else:
        res += int(updates[len(updates) // 2])

print(res)
print(res2)


