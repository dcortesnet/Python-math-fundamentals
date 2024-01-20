from sympy import symbols, Eq, solve

# Define the symbolic variable
x = symbols('x')

# Define the quadratic equation
quadratic_equation = Eq(x**2 - 4*x + 4, 0)

# Solve the equation
solutions = solve(quadratic_equation, x)

# Print the solutions
print("The solutions to the quadratic equation are x =", solutions)