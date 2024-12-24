from functools import cache

@cache
def dfs(test_string, towels):
    return not test_string or any(dfs(test_string[len(towel):], towels) for towel in towels if test_string.startswith(towel))

@cache
def dfs_p2(test_string, towels):
    return not test_string or sum(dfs_p2(test_string[len(towel):], towels) for towel in towels if test_string.startswith(towel))

towels = None
res = 0
res2 = 0
for line in open("input.txt"):
    line = line.strip()
    if towels is None:
        towels = line.split(", ")
        continue
    if not line:
        continue

    # Part 1
    res += dfs(line, tuple(towels))

    # Part 2
    res2 += dfs_p2(line, tuple(towels))

print(res)
print(res2)

