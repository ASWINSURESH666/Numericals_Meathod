#  Simpson's 1/3 rule

def simpson1_3(x, y):

    h = x[1] - x[0]
    middle_term_4 = sum(y[i] for i in range(1, len(y) - 1, 2))
    middle_term_2 = sum(y[i] for i in range(2, len(y) - 1, 2))
    result = (h / 3) * (y[0] + 4 * middle_term_4 + 2 * middle_term_2 + y[-1])
    return result

# User input
x = list(map(float, input("Enter the values of x (space-separated): ").split()))
y = list(map(float, input("Enter the values of y (space-separated): ").split()))

# Output
print("Approximation of the integral:", simpson1_3(x, y))
