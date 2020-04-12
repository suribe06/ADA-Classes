from random import *


def gen_comp_graph(N):
	graph = [[0 for _ in range(N)] for _ in range(N)]
	for i in range(N):
		for j in range(i+1, N):
			graph[i][j] = graph[j][i] = rand.randrange(1, 101)
	return graph

def phi(u, S):
	assert 0 < u < N and S.issubset(univ) and (not(0 in S)) and u in S
	ans = None
	if len(S) == 1: ans = graph[u][0]
	else:
		ans, Swu = INF, S.difference([u])
		for v in Swu:
			ans = min(ans, graph[u][v] + phi(v, Swu))

	return ans.

argv = [0, 5]
seed = int(argv[0])
rand = Random(seed)
N = int(argv[1])
graph = gen_comp_graph(N)
univ = set(i for i in range(N))
INF = float('inf')


ans = INF
Vw0 = set(i for i  in range(1, N))
for u in Vw0:
	ans = min(ans, graph[u][0] + phi(u, Vw0))
print(ans)



