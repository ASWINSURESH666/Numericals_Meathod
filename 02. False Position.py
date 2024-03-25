def regula_falsi(func, a, b, E):

    while True:
        c = (a * solve_fn(func, b) - b * solve_fn(func, a)) / (solve_fn(func, b) - solve_fn(func, a))

        if abs(solve_fn(func, c)) <= E:
            return c

        elif solve_fn(func, c) * solve_fn(func, a) < 0:
            b = c

        else:
            a = c


def solve_fn(eq, x):
    return eval(eq)


def main():
    eq = input("Enter x : ")
    E = float(input("Enter the value of ε: "))
    l = float(input("Enter the lower bound: "))
    u = float(input("Enter the upper bound: "))

    print("THE ROOT OF THE EQUATION IS:", regula_falsi(eq, l, u, E))


if __name__ == "__main__":
    main()
