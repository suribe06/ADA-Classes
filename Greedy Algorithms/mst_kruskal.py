def find(i):
    global parent
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]

def union(x, y):
    global parent, rank
    rx = find(x)
    ry = find(y)

    if rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] += 1

def kruskal(G, n):
    global parent, rank
    tree = []
    parent, rank = [], []
    G.sort(key=lambda x: x[2])
    for i in range(n):
        parent.append(i)
        rank.append(0)

    for u, v, w in G:
        x = find(u)
        y = find(v)
        if x != y:
            tree.append((u, v, w))
            union(x, y)

    return tree

G = [ (0, 1, 5),
      (0, 5, 4),
      (1, 2, 1),
      (1, 3, 8),
      (1, 7, 5),
      (2, 4, 4),
      (2, 5, 2),
      (2, 6, 1),
      (3, 4, 4),
      (5, 6, 3),
      (5, 7, 2),
      (6, 8, 6) ]

sol = kruskal(G, 9)
print(sol)
