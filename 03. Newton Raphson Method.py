import sympy as sp

def calculate_derivative(equation, variable='x'):
    x = sp.symbols(variable)
    expression = sp.sympify(equation)
    derivative = sp.diff(expression, x)
    return derivative

def newton_raphson(func, derivative_func, x0, tol=10^-6, max_iter=100):
    x = x0
    iterations = 0

    while abs(func(x)) > tol and iterations < max_iter:
        x = x - func(x) / derivative_func(x)
        iterations += 1

    return x, iterations

equation = input("Enter x : ")


x = sp.symbols('x')
user_function = sp.sympify(equation)
user_derivative = sp.diff(user_function, x)

func = sp.lambdify(x, user_function, 'numpy')
derivative_func = sp.lambdify(x, user_derivative, 'numpy')


initial_guess = float(input("\nEnter the first guessed root: "))

root, iterations = newton_raphson(func, derivative_func, initial_guess)

print(f"\nThe root of the equation is: {root}")
print(f"\nThe number of Iterations: {iterations}")
