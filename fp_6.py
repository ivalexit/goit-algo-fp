# Меню, ціна, калораж
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Ввід суми бюджету
def get_user_budget():
    while True:
        try:
            budget = int(input("Please enter your budget (at least 10): "))
            if budget >= 10:
                return budget
            else:
                print("Budget must be a positive integer of at least 10.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def greedy_algorithm(items, budget):
    # Сортування: калорії/вартість
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    # Вибір страв у межах бюджету
    for item, properties in sorted_items:
        if total_cost + properties['cost'] <= budget:
            selected_items.append(item)
            total_cost += properties['cost']
            total_calories += properties['calories']
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    # Створюємо списки вартостей і калорійності для зручного доступу
    item_names = list(items.keys())
    costs = [items[item]['cost'] for item in item_names]
    calories = [items[item]['calories'] for item in item_names]
    n = len(items)

    # Ініціалізація таблиці для динамічного програмування
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнення таблиці ДП
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Визначення обраних страв на основі таблиці ДП
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= costs[i - 1]

    total_calories = dp[n][budget]
    selected_items.reverse()  # Відновлюємо вихідний порядок вибору
    return selected_items, total_calories

# Виконання алгоритмів
if __name__ == "__main__":
    budget = get_user_budget()
    
    print("\nGreedy Algorithm:")
    greedy_selection, greedy_calories = greedy_algorithm(items, budget)
    print(f"Selected items: {greedy_selection}")
    print(f"Total calories: {greedy_calories}\n")

    print("Dynamic Programming Algorithm:")
    dp_selection, dp_calories = dynamic_programming(items, budget)
    print(f"Selected items: {dp_selection}")
    print(f"Total calories: {dp_calories}")