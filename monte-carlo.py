import random


def random_walk(n):
    x, y = 0, 0

    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (-1, 0)])
        x += dx
        y += dy
    return x, y


steps = int(input("Number of steps: "))

# example
for step in range(1, 31):
    barefoot = 0

    for i in range(steps):
        (x, y) = random_walk(step)
        distance = abs(x) + abs(y)

        if distance <= 4:
            barefoot += 1

    barefoot_percentage = float(barefoot) / steps
    print(f"Steps {barefoot} and % of barefoot = {100 * barefoot_percentage}")
