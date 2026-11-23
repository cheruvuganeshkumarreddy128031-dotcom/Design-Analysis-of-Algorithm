
n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (use 999 for infinity):")
dist = [list(map(int, input().split())) for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print("\nShortest Distance Matrix:")
for row in dist:
    print(*row)
