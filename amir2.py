import sympy as sp

# Display message
print("************In the name of God***********")
print("Please enter data to start the calculation process...")

# Define the function
x, y = sp.symbols('x y')
g = lambda x, y: (2/3) * (1 + x/12) * 1800 - 1200 * y / (1200 + 600 * x)

# Initial conditions
x_zero = 0
y_zero = 10
h = 0.01
x_final = 1

# Euler's method
while x_zero < x_final:
    y_zero += g(x_zero, y_zero) * h
    x_zero += h

print(f"Euler's Method Result: {y_zero}")

# Runge-Kutta 2
x_zero = 0
Y_zero = 10
while x_zero < x_final:
    k1 = g(x_zero, Y_zero)
    k2 = g(x_zero + h/2, Y_zero + (h/2) * k1)
    Y_zero += g(x_zero + h/2, Y_zero + (h/2) * k1) * h
    x_zero += h

print(f"Runge-Kutta 2 Result: {Y_zero}")

# Runge-Kutta 3
x_zero = 0
YY_zero = 10
while x_zero < x_final:
    k1 = g(x_zero, YY_zero)
    k2 = g(x_zero + h/2, YY_zero + (h/2) * k1)
    k3 = g(x_zero + h, YY_zero - k1 * h + 2 * k2 * h)
    YY_zero += (h/6) * (k1 + 4 * k2 + k3)
    x_zero += h

print(f"Runge-Kutta 3 Result: {YY_zero}")

# Runge-Kutta 4
x_zero = 0
YYY_zero = 10
while x_zero < x_final:
    k1 = g(x_zero, YYY_zero)
    k2 = g(x_zero + h/2, YYY_zero + (h/2) * k1)
    k3 = g(x_zero + h/2, YYY_zero + (h/2) * k2)
    k4 = g(x_zero + h, YYY_zero + h * k3)
    YYY_zero += (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)
    x_zero += h

print(f"Runge-Kutta 4 Result: {YYY_zero}")

# Comparisons
print(f"According to calculations, Euler's method provides the farthest result: {y_zero}")
print(f"Runge-Kutta 2 is more accurate than Euler's method: {Y_zero}")
print(f"Runge-Kutta 3 is more accurate than Runge-Kutta 2: {YY_zero}")
print(f"Finally, Runge-Kutta 4 is the most accurate method: {YYY_zero}")
print("Thanks for your attention...")