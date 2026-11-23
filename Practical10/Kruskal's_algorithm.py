
n = int(input("Enter vertices: "))
e = int(input("Enter edges: "))

edges = []
for i in range(e):
    u, v, w = map(int, input("Enter u v weight: ").split())
    edges.append((w, u, v))

edges.sort()
parent = list(range(n))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

cost = 0
print("\nMinimum Spanning Tree:")

for w, u, v in edges:
    a, b = find(u), find(v)
    if a != b:
        parent[a] = b
        print(u, "-", v, ":", w)
        cost += w

print("Minimum Cost:", cost)
