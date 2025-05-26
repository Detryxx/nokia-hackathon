from scipy.optimize import root_scalar
import sympy
import random

#first
R = sympy.symbols('R')
radius = sympy.Eq((((R - 2) / R) ** 2) + (((R - 1) / R) ** 2), 1)
solution_1 = sympy.solve(radius)
for i in solution_1:
    if i == 1:                      #this is because cos != 0 and if R = 1 then (R - 1) / R = 1 - 1 / 1 = 0 / 1 = 0
        solution_1.remove(i)
print(f"1.: {solution_1[0]}")


#second
def f(x):
    return 4**x + 6**x - 9**x

solution = root_scalar(f, bracket=[1, 2], method="brentq")
print(f"2.: {round(solution.root, 6)}")


#third
x = 1
solution_3 = 0
while x <= 99:
    solution_3 += (1 / ((x ** 0.5) +((x + 1) ** 0.5)))
    x = x + 1
print(f"3.: {round(solution_3)}")


#fourth
def g(x):
    return (x**x - 1)**2

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
for x in range(1250000):
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
