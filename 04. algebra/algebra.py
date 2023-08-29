import sympy as sp

x = sp.symbols('x')

equation = 3 * x - 5

solution = sp.solve(equation, x)

print("Solution:", solution) # [5/3]