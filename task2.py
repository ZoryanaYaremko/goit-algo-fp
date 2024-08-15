import matplotlib.pyplot as plt
import numpy as np

def draw_branch(x, y, angle, length, depth):
    if depth == 0:
        return

    # Обчислюємо кінцеві координати гілки
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # Малюємо гілку
    plt.plot([x, x_end], [y, y_end], color='brown', lw=2 * depth)

    # Нові гілки з новими кутами і довжинами
    new_length = length * 0.7  # Кожна наступна гілка коротша за попередню
    new_depth = depth - 1  # Зменшуємо глибину на 1

    # Рекурсивно малюємо дві нові гілки
    draw_branch(x_end, y_end, angle + np.pi / 4, new_length, new_depth)
    draw_branch(x_end, y_end, angle - np.pi / 4, new_length, new_depth)

# Налаштування вікна для малювання
plt.figure(figsize=(8, 8))
plt.axis('off')

# Запитуємо у користувача рівень рекурсії
depth = int(input("Введіть рівень рекурсії (глибину дерева): "))

# Початкова гілка
draw_branch(0, 0, np.pi / 2, 100, depth)

# Відображаємо фрактал
plt.show()
