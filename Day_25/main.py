import itertools

keys = []
locks = []

isLock = None
current = None
lock_dict = {True: "#", False: "."}

for line in open("input.txt"):
    line = line.strip()

    if not line:
        if isLock:
            locks.append(current)
        else:
            keys.append(current)

        isLock = None
        current = None
        continue

    if isLock is None:
        isLock = line[0] == "#"
        current = ((0, ) if isLock else (1, )) * len(line)
        continue

    current = tuple(current[i] + (char == lock_dict[isLock]) for i, char in enumerate(line))


if isLock:
    locks.append(current)
else:
    keys.append(current)

print(locks)
print(keys)

res = 0
for lock, key in itertools.product(locks, keys):
    if any(l >= k for l, k in zip(lock, key)):
        continue

    res += 1

print(res)
