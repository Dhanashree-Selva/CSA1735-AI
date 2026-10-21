
from itertools import permutations

def tsp(graph):
    n = len(graph)
    cities = range(1, n)
    min_cost = float('inf')
    best_path = []

    for p in permutations(cities):
        path = (0,) + p + (0,)
        cost = sum(
            graph[path[i]][path[i+1]]
            for i in range(n)
        )

        if cost < min_cost:
            min_cost = cost
            best_path = path

    print("Best Path:", best_path)
    print("Minimum Cost:", min_cost)

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp(graph)
