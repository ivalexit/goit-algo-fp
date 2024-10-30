## goit-algo-fp_7

# Використання методу Монте-Карло для підрахунку ймовірності випадання усіх можливих сум (2-12) на ігрових кубиках.

## Опис завдання
Метою даного завдання було написати програму на Python, яка імітує велику кількість кидків двох гральних кубиків, обчислює ймовірності сум чисел, що випали, та порівнює їх із теоретичними значеннями.

### Метод
Ми використали метод Монте-Карло, що передбачає:
1. Симуляцію мільйона кидків двох кубиків.
2. Обчислення частоти кожної можливої суми (від 2 до 12).
3. Підрахунок ймовірностей появи кожної суми, ділячи частоту появ на загальну кількість симуляцій.

## Результати
Результати, отримані методом Монте-Карло, дуже близькі до аналітичних ймовірностей, найменші та найбільші значення випадають рідше і з наближенням до середнього значення суми, ймовірність зромтає. Це свідчить про коректність розрахунків та ефективність методу.

| Сума | Ймовірність (Метод Монте-Карло) | Теоретична Ймовірність |
|------|---------------------------------|-------------------------|
| 2    | 2.80%                           | 2.78%                  |
| 3    | 5.58%                           | 5.56%                  |
| 4    | 8.38%                           | 8.33%                  |
| 5    | 11.15%                          | 11.11%                 |
| 6    | 13.91%                          | 13.89%                 |
| 7    | 16.61%                          | 16.67%                 |
| 8    | 13.89%                          | 13.89%                 |
| 9    | 11.07%                          | 11.11%                 |
| 10   | 8.31%                           | 8.33%                  |
| 11   | 5.53%                           | 5.56%                  |
| 12   | 2.77%                           | 2.78%                  |

## Висновок
Результати симуляції методом Монте-Карло дуже близькі до теоретичних значень, що підтверджує правильність розрахунків. Незначні відхилення пояснюються випадковістю у симуляції, але з ростом кількості кидків вони стають дедалі ближчими до аналітичних значень. Метод Монте-Карло є ефективним інструментом для моделювання ймовірностей подій, де аналітичні розрахунки також підтверджують отримані результати.