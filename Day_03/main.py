import re

# part 1
res = 0
for line in open("input.txt"):
    found = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)", line)

    for e in found:
        a, b = e.strip("mul()").split(",")
        res += int(a) * int(b)

print(res)


# part 2
res = 0
do = True
for line in open("input.txt"):
    found = re.findall("(mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don't\\(\\))", line)
    for e in found:
        if e == "do()":
            do = True
            continue
        if e == "don't()":
            do = False
            continue
        if do is False:
            continue
        a, b = e.strip("mul()").split(",")
        res += int(a) * int(b)

print(res)