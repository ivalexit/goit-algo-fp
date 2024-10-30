import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Задаємо кількість підкидань кубиків
num_rolls = 1_000_000

# Створюємо імітацію підкидань
dice1 = np.random.randint(1, 7, num_rolls)
dice2 = np.random.randint(1, 7, num_rolls)
sums = dice1 + dice2

# Підраховуємо частоту випадання кожної суми
sum_counts = {i: 0 for i in range(2, 13)}
for total in sums:
    sum_counts[total] += 1

# Обчислення ймовірності випадання кожної суми
sum_probabilities = {k: v / num_rolls for k, v in sum_counts.items()}

# Візуалізуємо результати таблицею:
print("Sum | Probability Monte Carlo M.  | Theoretical Probability")
print("------------------------------------------------------------")
theoretical_probabilities = ["2.78%", "5.56%", "8.33%", "11.11%", "13.89%", "16.67%", "13.89%", "11.11%", "8.33%", "5.56%", "2.78%"]
for i, (sum_value, probability) in enumerate(sum_probabilities.items(), start=2):
    print(f" {sum_value:>3}  |    {probability*100:>5.2f}%                 | {theoretical_probabilities[i-2]}")