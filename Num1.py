import numpy as np

print("****************In the name of God******************")
print("Please enter data to start the calculation process.")

# Input dimension of the matrix
n = int(input("Please enter the dimension of the matrix: "))
matrix_coefficient = np.zeros((n, n))

# Input matrix coefficients
for i in range(n):
    for j in range(n):
        matrix_coefficient[i, j] = float(input(f"Please enter element [{i+1}, {j+1}] of the matrix: "))

matrix_coefficient_real = matrix_coefficient.copy()
print("Matrix Coefficient:")
print(matrix_coefficient)

# Input constants
matrix_constants = np.zeros((n, 1))
for o in range(n):
    matrix_constants[o, 0] = float(input(f"Please enter constant for row {o+1}: "))

matrix_constant_second = matrix_constants.copy()

# Input guesses
matrix_guess = np.zeros((n, 1))
for d in range(n):
    matrix_guess[d, 0] = float(input(f"Please enter initial guess for x[{d+1}]: "))

matrix_guess_second = matrix_guess.copy()

# Check and pivot if necessary
for e in range(n):
    for y in range(1, n):
        if matrix_coefficient[e, e] == 0:
            v = matrix_coefficient[:, e].copy()
            matrix_coefficient[:, e] = matrix_coefficient[:, y]
            matrix_coefficient[:, y] = v
        else:
            break

print("Pivoted Matrix Coefficient:")
print(matrix_coefficient)

# Augment the coefficient matrix with constants
matrix_new = np.hstack((matrix_coefficient, matrix_constants))

# Forward elimination
for g in range(n):
    for p in range(g + 1, n):
        factor = matrix_new[p, g] / matrix_new[g, g]
        matrix_new[p, g:] -= factor * matrix_new[g, g:]

print("Matrix after forward elimination:")
print(matrix_new)

# Calculate determinant
determinant = np.prod([matrix_new[w, w] for w in range(n)])
print(f"Determinant is: {determinant}")

if determinant != 0:
    print("We have answers because the determinant is not zero.")
else:
    print("We have no answers because the determinant is zero.")

# Back substitution
x = np.zeros(n)
if determinant != 0:
    x[n-1] = matrix_new[n-1, n] / matrix_new[n-1, n-1]
    for t in range(n-2, -1, -1):
        x[t] = matrix_new[t, n] - np.dot(matrix_new[t, t+1:n], x[t+1:n])
        x[t] /= matrix_new[t, t]

print("Solution vector x:")
print(x)

# Iterative refinement
answer = np.zeros((n, 2 * n))
percentage = np.zeros((n, n))
h = np.zeros((n, 1))
summ_group = np.zeros((n, 1))
answer_list = np.zeros((n, 2))

for step in range(2):
    for aa in range(n):
        summ = 0
        for t in range(n):
            if t != aa:
                summ += matrix_coefficient[aa, t] * matrix_guess[t]
        h[aa, 0] = (matrix_constants[aa, 0] - summ) / matrix_coefficient[aa, aa]

        for u in np.arange(0.1, 2.1, 0.1):
            index = int((u - 0.1) / 0.1)
            b = u * h[aa, 0] + (1 - u) * matrix_guess[aa, 0]
            answer[index, step * n + aa] = b

        # Calculate errors
        for idx in range(answer.shape[0]):
            percentage[idx, aa] = abs((answer[idx, step * n + aa] - x[aa]) / x[aa]) * 100

    # Sum errors
    summ_group = np.sum(percentage, axis=1)
    min_index = np.argmin(summ_group)

    # Update guesses
    for y in range(n):
        matrix_guess[y, 0] = answer[min_index, step * n + y]

    answer_list[:, step] = matrix_guess[:, 0]

# Display final answers
for j in range(2):
    for k in range(n):
        print(f"x({k+1}) for step {j+1} = {answer_list[k, j]}")

# Check for unsuitable guesses
for j in range(2):
    if np.any(percentage[:, j] == np.sort(percentage[:, j])):
        print(f"Error: Your guess is unsuitable for this case. Please enter a new guess for x[{j+1}].")