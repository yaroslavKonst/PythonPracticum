"""Biquadratic equation solver"""
from sys import argv
from math import sqrt

A, B, C = map(int, argv[1:4])

D = B**2 - 4 * A * C
if D > 0:
    X1, X2 = (-B + sqrt(D)) / (2 * A), (-B - sqrt(D)) / (2 * A)
    F = False
    if X1 > 0:
        X1, F = sqrt(X1), True
        print(X1, -X1, end=(" " if X2 >= 0 else "\n"))
    elif X1 == 0:
        F = True
        print(X1, end=(" " if X2 >= 0 else "\n"))
    if X2 > 0:
        X2, F = sqrt(X2), True
        print(X2, -X2)
    elif X2 == 0:
        F = True
        print(X2)
    if not F:
        print("No roots")
elif D == 0:
    X = -B / (2 * A)
    if X > 0:
        X = sqrt(X)
        print(X, -X)
    elif X == 0:
        print(X)
    else:
        print("No roots")
else:
    print("No roots")
