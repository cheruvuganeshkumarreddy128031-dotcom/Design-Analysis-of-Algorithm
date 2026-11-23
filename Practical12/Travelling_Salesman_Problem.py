
from itertools import permutations

n = int(input("Enter number of cities: "))

print("Enter cost matrix:")
cost = [list(map(int, input().split())) for i in range(n)]

min_cost = float('inf')
best_path = None

for path in permutations(range(1, n)):
    route = (0,) + path + (0,)
    total = sum(cost[route[i]][route[i+1]] for i in range(n))

    if total < min_cost:
        min_cost = total
        best_path = route

print("Shortest Path:", best_path)
print("Minimum Cost:", min_cost)
