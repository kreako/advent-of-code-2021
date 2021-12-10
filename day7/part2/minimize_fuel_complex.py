import math


def cost(l, p):
    return sum([abs(x - p) * (abs(x - p) + 1) / 2 for x in l])


def minimize_cost(l):
    l_min = min(l)
    l_max = max(l)

    min_cost = math.inf
    for i in range(l_min, l_max + 1):
        min_cost = min(min_cost, cost(l, i))

    return min_cost


if __name__ == "__main__":
    little = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    print(minimize_cost(little))

    with open("../input", "r") as f:
        l = [int(x) for x in f.read().split(",")]

    print(minimize_cost(l))
