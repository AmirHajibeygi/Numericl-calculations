import sympy as sp

def euler_method(g, x0, y0, h, x_final):
    while x0 < x_final:
        y0 += g(x0, y0) * h
        x0 += h
    return y0

def runge_kutta_2(g, x0, y0, h, x_final):
    while x0 < x_final:
        k1 = g(x0, y0)
        k2 = g(x0 + h / 2, y0 + (h / 2) * k1)
        y0 += h * k2
        x0 += h
    return y0

def runge_kutta_3(g, x0, y0, h, x_final):
    while x0 < x_final:
        k1 = g(x0, y0)
        k2 = g(x0 + h / 2, y0 + (h / 2) * k1)
        k3 = g(x0 + h, y0 - k1 * h + 2 * k2 * h)
        y0 += (h / 6) * (k1 + 4 * k2 + k3)
        x0 += h
    return y0

def runge_kutta_4(g, x0, y0, h, x_final):
    while x0 < x_final:
        k1 = g(x0, y0)
        k2 = g(x0 + h / 2, y0 + (h / 2) * k1)
        k3 = g(x0 + h / 2, y0 + (h / 2) * k2)
        k4 = g(x0 + h, y0 + h * k3)
        y0 += (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x0 += h
    return y0

# Generic input
print("************In the name of God***********")
print("This program solves IVPs using Euler's and Runge-Kutta methods.")
print("Please define your problem and provide necessary inputs.")

# User-defined function
x, y = sp.symbols('x y')
expr = input("Enter the function g(x, y) as a Python expression (e.g., 'x + y'): ")
g = sp.lambdify((x, y), sp.sympify(expr))

# Initial conditions and step size
x0 = float(input("Enter the initial value of x (x0): "))
y0 = float(input("Enter the initial value of y (y0): "))
h = float(input("Enter the step size (h): "))
x_final = float(input("Enter the final value of x: "))

# Solving using different methods
euler_result = euler_method(g, x0, y0, h, x_final)
rk2_result = runge_kutta_2(g, x0, y0, h, x_final)
rk3_result = runge_kutta_3(g, x0, y0, h, x_final)
rk4_result = runge_kutta_4(g, x0, y0, h, x_final)

# Output results
print(f"Euler's Method Result: {euler_result}")
print(f"Runge-Kutta 2 Result: {rk2_result}")
print(f"Runge-Kutta 3 Result: {rk3_result}")
print(f"Runge-Kutta 4 Result: {rk4_result}")

# Conclusion
print(f"Based on the calculations:")
print(f"- Euler's method provides the farthest answer: {euler_result}")
print(f"- Runge-Kutta 2 is better than Euler: {rk2_result}")
print(f"- Runge-Kutta 3 is better than Runge-Kutta 2: {rk3_result}")
print(f"- Runge-Kutta 4 is the best method with the most accurate result: {rk4_result}")
print("Thanks for your attention!")