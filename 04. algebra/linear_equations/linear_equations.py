from sympy import symbols, Eq, solve

# Define the symbolic variable
x = symbols('x')

# Define the linear equation
equation = Eq(3*x + 5, 11)

# Solve the equation
solution = solve(equation, x)

# Print the solution
print("The solution to the equation is x =", solution[0])
