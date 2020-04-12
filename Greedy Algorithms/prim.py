from sys import stdin
from heapq import heappush,heappop

def prim(G):
	ans = list()
	pq = list()
	for u,v,w in G[0]: heappush(pq,(w,u,v))
	visited = [False for _ in G] ; visited[0] = True
	while len(pq)!=0:
		w,u,v = heappop(pq)
		if (visited[v] == False):
			visited[v] = True
			ans.append((u,v,w))
			for tu, tv, tw in G[v]: heappush(pq,(tw,tu,tv))
	return ans

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

sol = prim(G)
print(sol)
