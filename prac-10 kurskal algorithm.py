def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal(edges, V):
    edges.sort(key=lambda x: x[2])

    parent = list(range(V))
    rank = [0] * V

    total_cost = 0
    count = 0

    print("Edges in Minimum Spanning Tree:")

    for u, v, w in edges:
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            print(u, "-", v, ":", w)
            total_cost += w
            union(parent, rank, x, y)
            count += 1

            if count == V - 1:
                break

    if count != V - 1:
        print("MST does not exist")
    else:
        print("Total Minimum Cost:", total_cost)


V = 4

edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

kruskal(edges, V)
