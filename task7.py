import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    # Підрахунок кількості кидків для можливих значень сум
    sums_count = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        sum_of_rolls = roll1 + roll2
        sums_count[sum_of_rolls] += 1
    
    # Обчислення ймовірностей випадання кожної суми
    probabilities = {sum_: count / num_rolls for sum_, count in sums_count.items()}
    
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    # Створення графіка
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')
    
    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')
    
    plt.show()

if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        print(f"\nСимуляція для {accuracy} кидків:")
        # Симуляція кидків і обчислення ймовірностей
        probabilities = simulate_dice_rolls(accuracy)
        
        # Виведення результатів у консоль
        for sum_, prob in sorted(probabilities.items()):
            print(f"Сума {sum_}: Ймовірність {prob*100:.2f}%")
        
        # Відображення ймовірностей на графіку
        plot_probabilities(probabilities)
