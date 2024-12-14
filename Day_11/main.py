from functools import cache

stones = []
for line in open("input.txt"):
    stones = [int(num) for num in line.split()]


# caching is mandatory
@cache
def recursive_seeker(stone, depth, max_depth):
    if depth >= max_depth:
        return 1

    if stone == 0:
        return recursive_seeker(1, depth + 1, max_depth)

    if len(x := str(stone)) % 2 == 0:
        return (recursive_seeker(int(x[0:len(x) // 2]), depth + 1, max_depth) +
                recursive_seeker(int(x[len(x) // 2:len(x)]), depth + 1, max_depth))

    return recursive_seeker(stone * 2024, depth + 1, max_depth)


res = 0
res2 = 0
for stone in stones:
    res += recursive_seeker(stone, 0, 25)  # Part 1
    res2 += recursive_seeker(stone, 0, 75)  # Part 2

print(res)
print(res2)
