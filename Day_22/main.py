from functools import cache
from itertools import pairwise

# code could have been more optimised

#@cache
def get_code(number):
    number = ((number * 64) ^ number) % 16777216
    number = ((number // 32) ^ number) % 16777216
    number = ((number * 2048) ^ number) % 16777216

    return number


def shift(history, new_val):
    for i in range(len(history) - 1, 0, -1):
        history[i] = history[i - 1]

    history[0] = new_val


#def get_diffs(history):
#    return tuple(reversed(tuple(n - m for n, m in pairwise(history))))

def get_diffs(h):
    return h[3] - h[4], h[2] - h[3], h[1] - h[2], h[0] - h[1]


res = 0
seq_values = {}

for line in open("input.txt"):
    line = line.strip()
    num = int(line)

    history = [num % 10, None, None, None, None]
    for i in range(2000):
        num = get_code(num)

        shift(history, num % 10)
        if any(e is None for e in history):
            continue

        diffs = get_diffs(history)

        if seq_values.get(diffs, (True, True))[1] is False:
            continue

        seq_values[diffs] = (seq_values.get(diffs, (0, 0))[0] + num % 10, False)

    for diffs in seq_values:
        seq_values[diffs] = (seq_values[diffs][0], True)

    res += num

print(res)
print(max(seq_values.items(), key=lambda e: e[1][0]))

