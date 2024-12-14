import math
import re

from sympy.solvers.diophantine import diop_solve
from sympy import symbols

x, y, t_0, t = symbols("x, y, t_0, t", integer=True)


res = 0
res2 = 0
with open("input.txt") as file:
    lines = [line.strip() for line in file if line.strip()]

    for button_a, button_b, prize in zip(lines[::3], lines[1::3], lines[2::3]):

        a1, a2 = re.findall(r"[0-9]+", button_a)
        b1, b2 = re.findall(r"[0-9]+", button_b)
        c1, c2 = re.findall(r"[0-9]+", prize)

        a1, a2, b1, b2, c1, c2 = int(a1), int(a2), int(b1), int(b2), int(c1), int(c2)
        determinant = 1 / (a1 * b2 - a2 * b1)

        # Part 1
        a_tokens = round(determinant * (b2 * c1 - b1 * c2))
        b_tokens = round(determinant * (-a2 * c1 + a1 * c2))

        if a_tokens * a1 + b_tokens * b1 == c1 and a_tokens * a2 + b_tokens * b2 == c2:
            res += 3 * a_tokens + 1 * b_tokens


        # Part 2
        c1, c2 = c1 + 10000000000000, c2 + 10000000000000
        a_tokens = round(determinant * (b2 * c1 - b1 * c2))
        b_tokens = round(determinant * (-a2 * c1 + a1 * c2))

        if a_tokens * a1 + b_tokens * b1 == c1 and a_tokens * a2 + b_tokens * b2 == c2:
            res2 += 3 * a_tokens + 1 * b_tokens



        """a = sum((int(n) for n in re.findall(r"[0-9]+", button_a)))
        b= sum((int(n) for n in re.findall(r"[0-9]+", button_b)))
        c = sum((int(n) for n in re.findall(r"[0-9]+", prize)))

        eq1, eq2 = diop_solve(a*x + b*y - c)

        if eq1 is None or eq2 is None:
            continue

        #print(eq1, eq2)

        q11, q12 = re.findall(r"(-?[0-9]+\*?t?_?0?)", str(eq1).replace(" ", ""))
        q21, q22 = re.findall(r"(-?[0-9]+\*?t?_?0?)", str(eq2).replace(" ", ""))

        #print(eq1, ":", q11, q12, "\\n", eq2, ":", q21, q22)
        q1 = int(q12) / int(q11.replace("*t_0", "")) if "*t_0" in q11 else int(q11) / int(q12.replace("*t_0", ""))
        q2 = int(q22) / int(q21.replace("*t_0", "")) if "*t_0" in q21 else int(q21) / int(q22.replace("*t_0", ""))

        #print(q11, q12, ":", q1,"\\t" , q21, q22, ":", q2)
        if -math.floor(q1) > -round(q2) + 1:
            print("nene")

        for k in range(-math.floor(q1), -math.ceil(q2) + 1):
            a_tokens = eq1.subs({t_0:k})
            b_tokens = eq2.subs({t_0:k})
            #print(a_tokens, b_tokens)
            if 0 <= a_tokens <= 100 and 0 <= b_tokens <= 100:
                res += 3 * a_tokens + 1 * b_tokens
                break

        else:
            print(q1, q2)
            print(-math.floor(q1), -int(q2) + (-2 if abs(q2) == q2 else 2))
            print()
            pass"""

print(res)
print(res2)

