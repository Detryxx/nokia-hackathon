# pylint: disable=C0103
"""
    random - needed for the randomization of die rolls in exercise 7
    scipy - needed for the root_scalar for the second exercise
    sympy - needed for solving linear equations (exercise 5, 6)

    comments - or rather my thought process - can be found in the thinking.txt file as described per
    the exercise
"""
import random
from scipy.optimize import root_scalar
import sympy


#first
R = sympy.symbols('R')
radius = sympy.Eq((((R - 2) / R) ** 2) + (((R - 1) / R) ** 2), 1)
solution_1 = sympy.solve(radius)
for i in solution_1:
    if i == 1:  #this is because cos != 0 and if R = 1 then (R - 1) / R = 1 - 1 / 1 = 0 / 1 = 0
        solution_1.remove(i)
print(f"1.: {solution_1[0]}")


#second
def f(x):
    """
        Defines the function f(x) for the second exercise
    """
    return 4**x + 6**x - 9**x

solution = root_scalar(f, bracket=[1, 2], method="brentq")
print(f"2.: {round(solution.root, 6)}")


#third
y = 1
solution_3 = 0
while y <= 99:
    solution_3 += (1 / ((y ** 0.5) +((y + 1) ** 0.5)))
    y = y + 1
print(f"3.: {round(solution_3)}")


#fourth
def g(z):
    """
        Defines the function g(z) for the fourth exercise
    """
    return (z**z - 1)**2

solution = root_scalar(g, bracket=[0.5, 1.5], method="newton", x0 = 1)
print(f"4.: {solution.root}")


#fifth
a, t, c = sympy.symbols('a t c')

equation1 = sympy.Eq(a - t + c, 170)
equation2 = sympy.Eq(a - c + t, 130)

solution_5 = sympy.solve((equation1, equation2))
print(f"5.: {solution_5[a]}")


#sixth
c, e, k, t = sympy.symbols('c e k t')

eq1 = sympy.Eq(c + e, 10)
eq2 = sympy.Eq(k + e, 20)
eq3 = sympy.Eq(k + c, 24)
eq4 = sympy.Eq(c + k + e, t)

solution_6 = sympy.solve((eq1, eq2, eq3, eq4))
print(f"6.: {solution_6[t]}")


#seventh
Anna = []
Balazs = []
winners = []
for i in range(1250000):
    while True:
        dice_roll = random.randint(1, 6)
        Anna.append(dice_roll)
        if 6 in Anna:
            winners.append("A")
            break
        dice_roll = random.randint(1, 6)
        Balazs.append(dice_roll)
        if 6 in Balazs:
            winners.append("B")
            break
    Anna = []
    Balazs = []
Anna_win = winners.count("A")
Balazs_win = winners.count("B")
A_win_perc = Anna_win / (Balazs_win + Anna_win)
print(f"7.: {round(A_win_perc * 100, 6)}%")
