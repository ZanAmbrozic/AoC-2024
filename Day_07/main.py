
# Part 1
def operator_check(numbers, curr_value, test_val):
    if not numbers:
        return curr_value == test_val
    if curr_value > test_val:
        return False

    return (operator_check(numbers[1:], curr_value + int(numbers[0]), test_val) or
            operator_check(numbers[1:], curr_value * int(numbers[0]), test_val))


# Part 2
def operator_check_with_concat(numbers, curr_value, test_val):
    if not numbers:
        return curr_value == test_val
    if curr_value > test_val:
        return False

    return (operator_check_with_concat(numbers[1:], curr_value + int(numbers[0]), test_val) or
            operator_check_with_concat(numbers[1:], curr_value * int(numbers[0]), test_val) or
            operator_check_with_concat(numbers[1:], int(str(curr_value) + numbers[0]), test_val))


res = 0
res2 = 0
for line in open("input.txt"):

    test_val, *numbers = line.split()
    test_val = int(test_val.strip(":"))

    res += test_val if operator_check(numbers[1:], int(numbers[0]), test_val) else 0
    res2 += test_val if operator_check_with_concat(numbers[1:], int(numbers[0]), test_val) else 0


print(res)
print(res2)

