def prim(graph, n):
    selected = [False] * n
    selected[0] = True

    total_cost = 0

    print("Edges in Minimum Spanning Tree:")

    for i in range(n - 1):
        min_cost = float('inf')
        x = 0
        y = 0

        for j in range(n):
            if selected[j]:
                for k in range(n):
                    if not selected[k] and graph[j][k] != 0:
                        if graph[j][k] < min_cost:
                            min_cost = graph[j][k]
                            x = j
                            y = k

        print(x, "-", y, ":", min_cost)

        selected[y] = True
        total_cost += min_cost

    print("Total Minimum Cost:", total_cost)


graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim(graph, 5)
