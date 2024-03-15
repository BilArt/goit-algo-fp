def greedy_algorithm(foods, budget):
    sorted_foods = sorted(foods, key=lambda x: x['calories'] / x['cost'], reverse=True)
    
    selected_foods = []
    total_calories = 0
    total_cost = 0
    
    for food in sorted_foods:
        if total_cost + food['cost'] <= budget:
            selected_foods.append(food['name'])
            total_calories += food['calories']
            total_cost += food['cost']
    
    return selected_foods, total_calories, total_cost

def dynamic_programming(foods, budget):
    n = len(foods)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if foods[i - 1]['cost'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - foods[i - 1]['cost']] + foods[i - 1]['calories'])
            else:
                dp[i][j] = dp[i - 1][j]
    
    selected_foods = []
    total_calories = dp[n][budget]
    total_cost = budget
    j = budget
    
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_foods.append(foods[i - 1]['name'])
            j -= foods[i - 1]['cost']
            total_cost -= foods[i - 1]['cost']
    
    return selected_foods, total_calories, budget - total_cost

# Приклад використання:
foods = [
    {'name': 'Салат', 'calories': 100, 'cost': 20},
    {'name': 'Суп', 'calories': 200, 'cost': 30},
    {'name': 'Гаряче', 'calories': 300, 'cost': 40},
    {'name': 'Десерт', 'calories': 150, 'cost': 25},
    {'name': 'Напій', 'calories': 50, 'cost': 10}
]

budget = 60

selected_foods_greedy, total_calories_greedy, total_cost_greedy = greedy_algorithm(foods, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", selected_foods_greedy)
print("Загальна кількість калорій:", total_calories_greedy)
print("Всього витрачено:", total_cost_greedy)

selected_foods_dp, total_calories_dp, total_cost_dp = dynamic_programming(foods, budget)
print("\nДинамічне програмування:")
print("Вибрані страви:", selected_foods_dp)
print("Загальна кількість калорій:", total_calories_dp)
print("Всього витрачено:", total_cost_dp)
