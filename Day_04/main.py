
letters = []
for line in open("input.txt"):
    letters.append("..." + line.strip() + "...")

letters = ["." * len(letters[0])] * 3 + letters + ["." * len(letters[0])] * 3

# part 1

res = 0
for i in range(3, len(letters) - 3):
    for j in range(3, len(letters[0]) - 3):
        if letters[i][j] != "X":
            continue
        # up
        if letters[i + 1][j] == "M" and letters[i + 2][j] == "A" and letters[i + 3][j] == "S":
            res += 1
        # down
        if letters[i - 1][j] == "M" and letters[i - 2][j] == "A" and letters[i - 3][j] == "S":
            res += 1
        # left
        if letters[i][j - 1] == "M" and letters[i][j - 2] == "A" and letters[i][j - 3] == "S":
            res += 1
        # right
        if letters[i][j + 1] == "M" and letters[i][j + 2] == "A" and letters[i][j + 3] == "S":
            res += 1
        # up + right
        if letters[i + 1][j + 1] == "M" and letters[i + 2][j + 2] == "A" and letters[i + 3][j + 3] == "S":
            res += 1
        # down + right
        if letters[i - 1][j + 1] == "M" and letters[i - 2][j + 2] == "A" and letters[i - 3][j + 3] == "S":
            res += 1
        # up + left
        if letters[i + 1][j - 1] == "M" and letters[i + 2][j - 2] == "A" and letters[i + 3][j - 3] == "S":
            res += 1
        # down + left
        if letters[i - 1][j - 1] == "M" and letters[i - 2][j - 2] == "A" and letters[i - 3][j - 3] == "S":
            res += 1

print(res)


res = 0
for i in range(3, len(letters) - 3):
    for j in range(3, len(letters[0]) - 3):
        if letters[i][j] != "A":
            continue
        # case one
        if (letters[i + 1][j - 1] == "M" and letters[i + 1][j + 1] == "M"
                and letters[i - 1][j - 1] == "S" and letters[i - 1][j + 1] == "S"):
            res += 1

        # case two
        if (letters[i + 1][j - 1] == "S" and letters[i + 1][j + 1] == "S"
                and letters[i - 1][j - 1] == "M" and letters[i - 1][j + 1] == "M"):
            res += 1

        # case three
        if (letters[i + 1][j - 1] == "S" and letters[i + 1][j + 1] == "M"
                and letters[i - 1][j - 1] == "S" and letters[i - 1][j + 1] == "M"):
            res += 1

        # case four
        if (letters[i + 1][j - 1] == "M" and letters[i + 1][j + 1] == "S"
                and letters[i - 1][j - 1] == "M" and letters[i - 1][j + 1] == "S"):
            res += 1

print(res)