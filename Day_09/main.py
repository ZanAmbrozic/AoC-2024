# very suboptimal solution

memory = []
i = 0
adding_block = True

for line in open("input.txt"):
    for char in line.strip():
        if char == "0":
            i += 1 if adding_block else 0
            adding_block = not adding_block
            continue
        if adding_block is False:
            adding_block = True
            #memory += ["." for _ in range(int(char))]
            memory += [["." for _ in range(int(char))]]
            continue

        adding_block = False
        #memory += [str(i) for _ in range(int(char))]
        memory += [[str(i) for _ in range(int(char))]]
        i += 1

# Part 1

res = 0
mem = [j for i in memory for j in i]
for i, char in enumerate(mem[:len(mem) - mem.count(".")]):
    if char != ".":
        res += i * int(char)
        continue

    while mem[-1] == ".":
        del mem[-1]
    res += i * int(mem[-1])
    del mem[-1]

print(res)


# Part 2

mem = [j for i in memory for j in i]
i = len(mem) - 1
while i >= 0:
    char = mem[i]
    if char == ".":
        i -= 1
        continue

    block_len = 0
    for c in mem[i::-1]:
        if c != char:
            break
        block_len += 1

    for j, test_char in enumerate(mem[:i]):
        if test_char != ".":
            continue

        test_block_len = 0
        for c in mem[j:]:
            if c != ".":
                break
            test_block_len += 1

        if test_block_len < block_len:
            continue

        for k in range(block_len):
            mem[i - k], mem[j + k] = mem[j + k], mem[i - k]
        break
    i -= block_len


res = 0
for i, char in enumerate(mem):
    if char == ".":
        continue
    res += i * int(char)

print(res)
