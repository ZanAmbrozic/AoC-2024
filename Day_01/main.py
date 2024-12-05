left_list = []
right_list = []
for line in open("input.txt"):
    l, r = line.split()
    left_list.append(int(l))
    right_list.append(int(r))


# part 1
res = sum(abs(l - r) for l, r in zip(sorted(left_list), sorted(right_list)))

print(res)


# part 2
res = sum(e * right_list.count(e) for e in left_list)

print(res)