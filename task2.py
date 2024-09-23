import math

# Інтервал [a, b] і крок h
a = -1
b = 1
h = 0.5
d = 0.001  # похибка

# Функція для обчислення ряду
def calculate_series(x, d):
    k = 1
    sum_series = 0
    term = float('inf')  # початкове значення, більше похибки
    
    while abs(term) > d:
        term = ((-1) ** k * x) / (k * (k + 1)) - math.sin(2 * k + 1)
        sum_series += term
        k += 1
    
    return sum_series

# Початкове значення x
x = a

# Табуляція функцій
while x <= b:
    result = calculate_series(x, d)
    print(f"x = {x:.2f}, f(x) = {result:.6f}")
    
    # Збільшуємо x на крок h
    x += h
