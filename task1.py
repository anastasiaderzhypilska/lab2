import math

# Інтервал [a, b] і крок h
a = 0.5
b = 0.8
h = 0.02

# Початкове значення x
x = a

# Табуляція функцій
while x <= b:
    if x < 0.6:
        result = math.exp(x - math.sin(x))  # e^(x - sin(x))
    elif 0.6 <= x < 0.7:
        result = math.tan(abs(math.log(x)))  # tg(|ln(x)|)
    else:
        result = math.atan(x ** 7)  # arctg(x^7)
    
    print(f"x = {x:.2f}, f(x) = {result:.4f}")
    
    # Збільшуємо x на крок h
    x += h
