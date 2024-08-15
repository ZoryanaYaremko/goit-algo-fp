import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


# Дані про страви
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    # Сортуємо страви за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    for item, details in sorted_items:
        if details["cost"] <= remaining_budget:
            chosen_items.append(item)
            total_calories += details["calories"]
            remaining_budget -= details["cost"]

    return total_calories, budget - remaining_budget, chosen_items

# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(items)

    # Створення DP таблиці (рядки: страви, колонки: бюджет)
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо таблицю DP
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if items[item_names[i-1]]["cost"] <= w:
                dp_table[i][w] = max(dp_table[i-1][w], dp_table[i-1][w - items[item_names[i-1]]["cost"]] + items[item_names[i-1]]["calories"])
            else:
                dp_table[i][w] = dp_table[i-1][w]

    # Визначаємо вибір продуктів
    total_calories = dp_table[n][budget]
    chosen_items = []
    w = budget

    for i in range(n, 0, -1):
        if total_calories <= 0:
            break
        if total_calories == dp_table[i-1][w]:
            continue
        else:
            chosen_items.append(item_names[i-1])
            total_calories -= items[item_names[i-1]]["calories"]
            w -= items[item_names[i-1]]["cost"]

    chosen_items.reverse()  # Для зручності перегляду обраних продуктів у порядку додавання
    return dp_table[n][budget], budget - w, chosen_items


if __name__ == '__main__':
    budget = 100

    # Виконуємо обидва алгоритми
    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Greedy Algorithm Result: ", greedy_result)
    print("Dynamic Programming Result: ", dp_result)

# greedy_algorithm вибирає страви на основі найвищого співвідношення калорій до вартості, поки бюджет не вичерпаний.
# dynamic_programming будує таблицю динамічного програмування, де кожна клітинка представляє максимальну кількість калорій, яку можна отримати за певний бюджет. Він гарантує оптимальне рішення.