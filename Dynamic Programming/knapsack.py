

def knapsack(B, W, m, n, memo):
	ans, key = None, (n, m)
	if key in memo: ans = memo[key]
	else:
		if n == 0:
			ans = 0
		else:
			ans = knapsack(B, W, m, n-1, memo)
			if W[n-1] <= m:
				ans = max(ans, B[n-1] + knapsack(B, W, m - W[n-1], n-1, memo))
		memo[key] = ans
	return ans


def knapsack_tab(B, W, M):
	N = len(B)
	tab = [[None for _ in range(M+1)] for _ in range(N+1)]
	for m in range(M+1): tab[0][m] = 0
	n, m = 1, 0
	while n != N+1:
		if m == M+1:
			n, m = n+1, 0
		else:
			tab[n][m] = tab[n-1][m]
			if W[n-1] <= m:
				tab[n][m] = max(tab[n][m], B[n-1] + tab[n-1][m-W[n-1]])
			m += 1
	return tab[N][M]



def main():
	B = [3, 7, 5]
	W = [2, 4, 3]
	n = len(B)
	m = 4
	print(knapsack(B, W, m, n))
	#print(knapsack_tab(B, W, m))

main()
