import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return (x - 15)**2 + 5

# Метод половинного деления
def bisection_method(f, a, b, tol=1e-5):
    c = (a + b) / 2  # Точка половины
    if f(a) < f(b):
        b = c
    else:
        a = c
    return a, b, c

# Метод золотого сечения
def golden_section_method(f, a, b, tol=1e-5):
    phi = (1 + np.sqrt(5)) / 2  # Золотое число
    resphi = 2 - phi

    x1 = a + resphi * (b - a)
    x2 = b - resphi * (b - a)

    if f(x1) < f(x2):
        b = x2
    else:
        a = x1

    return a, b, x1, x2

# Метод Фибоначчи

def fibonacci_method(f, a, b, n=10):
    fib = [0, 1]
    for i in range(2, n + 2):
        fib.append(fib[-1] + fib[-2])

    rho = 1 - fib[n] / fib[n + 1]


   
    return}\gfed
