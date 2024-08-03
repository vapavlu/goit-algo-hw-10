import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0
b = 2

# Метод Монте-Карло
def monte_carlo_integration(f, a, b, num_samples):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = f(x_random)
    integral_estimate = (b - a) * np.mean(y_random)
    return integral_estimate

num_samples = 10000
monte_carlo_result = monte_carlo_integration(f, a, b, num_samples)

# Точне обчислення інтеграла
exact_result, _ = spi.quad(f, a, b)

print(f"Інтеграл (метод Монте-Карло): {monte_carlo_result}")
print(f"Інтеграл (функція quad): {exact_result}")
