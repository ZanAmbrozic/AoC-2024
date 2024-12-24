import re

lines = open("input.txt").readlines()

a = int(next(re.finditer(r"[0-9,]+", lines[0])).group())
b = int(next(re.finditer(r"[0-9,]+", lines[1])).group())
c = int(next(re.finditer(r"[0-9,]+", lines[2])).group())

program = [int(e.group()) for e in re.finditer(r"[0-9]", lines[4])]

pointer = 0
output = []

while pointer < len(program):
    opcode = program[pointer]
    c_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c}

    opr = program[pointer + 1]
    match opcode:
        case 0:
            a = a // (2 ** c_operands[opr])
        case 1:
            b = b ^ opr
        case 2:
            b = c_operands[opr] % 8
        case 3:
            if a == 0:
                pointer += 2
            else:
                pointer = opr
            continue
        case 4:
            b = b ^ c
        case 5:
            output.append(c_operands[opr] % 8)
        case 6:
            b = a // (2 ** c_operands[opr])
        case 7:
            c = a // (2 ** c_operands[opr])

    #print(oct(a))
    pointer += 2

#print(output)
print(",".join(map(str, output)))


# Part 2

def get_output(a, program):
    b = 0
    c = 0
    pointer = 0
    output = []

    while pointer < len(program):
        opcode = program[pointer]
        c_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c}

        opr = program[pointer + 1]
        match opcode:
            case 0:
                a = a // (2 ** c_operands[opr])
            case 1:
                b = b ^ opr
            case 2:
                b = c_operands[opr] % 8
            case 3:
                if a == 0:
                    pointer += 2
                else:
                    pointer = opr
                continue
            case 4:
                b = b ^ c
            case 5:
                output.append(c_operands[opr] % 8)
            case 6:
                b = a // (2 ** c_operands[opr])
            case 7:
                c = a // (2 ** c_operands[opr])

        pointer += 2
    return output

def dfs(a, program):
    if len(str(oct(a))) - 2 == len(program):
        return a

    res = 0
    for i in range(a == 0, 8):
        test_a = 8 * a + i
        test_out = get_output(test_a, program)
        if test_out[::-1] == list(reversed(program))[:len(test_out):]:
            res = dfs(test_a, program)
            if res != 0:
                return res

    return res


print(dfs(0, program))


