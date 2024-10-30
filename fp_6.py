# Меню, вартість, калорійність
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Ввід суми бюджету користувача
def get_user_budget():
    while True:
        try:
            budget = int(input("Please enter your budget (at least 10):  "))
            if budget >= 10:
                return budget
            else:
                print("Budget must be a positive integer of at least 10.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def greedy_algorithm(items, budget):
    # Сортування калорії/вартість
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    chosen_items = []
    total_cost = 0
    total_calories = 0

    for item, properties in sorted_items:
        if total_cost + properties["cost"] <= budget:
            chosen_items.append(item)
            total_cost += properties["cost"]
            total_calories += properties["calories"]
    
    return chosen_items, total_calories
