from pulp import LpMaximize, LpProblem, LpVariable, value

# Створення проблеми оптимізації
model = LpProblem(name="beverage-production", sense=LpMaximize)

# Змінні: кількість одиниць виробництва кожного напою
lemonade = LpVariable(name="lemonade", lowBound=0, cat="Continuous")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Continuous")

# Обмеження ресурсів
model += (2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint")
model += (1 * lemonade <= 50, "Sugar_Constraint")
model += (1 * lemonade <= 30, "LemonJuice_Constraint")
model += (2 * fruit_juice <= 40, "FruitPuree_Constraint")

# Мета: максимізація загальної кількості вироблених продуктів
model += (lemonade + fruit_juice, "Total_Production")

# Розв'язання моделі
model.solve()

# Виведення результатів
print(f"Кількість Лимонаду для виробництва: {lemonade.varValue:.2f}")
print(f"Кількість Фруктового соку для виробництва: {fruit_juice.varValue:.2f}")
print(f"Максимальна кількість продуктів: {value(model.objective):.2f}")
