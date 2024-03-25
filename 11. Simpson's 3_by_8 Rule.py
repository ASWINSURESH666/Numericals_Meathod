#  Simpson's 3/8 rule

def simpson3_8(x, y):

    h = x[1] - x[0]
    middle_term_3 = sum(y[i] for i in range(1, len(y) - 1) if i % 3 != 0)
    middle_term_2 = sum(y[i] for i in range(1, len(y) - 1) if i % 3 == 0)
    result = ((3 * h) / 8) * (y[0] + 3 * middle_term_3 + 2 * middle_term_2 + y[-1])
    return result

# User input
x = list(map(float, input("Enter the values of x (space-separated): ").split()))
y = list(map(float, input("Enter the values of y (space-separated): ").split()))

# Output
print("Approximation of the integral:", simpson3_8(x, y))
