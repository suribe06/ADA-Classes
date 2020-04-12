from sys import stdin

INF = -float('inf')
mem = dict()
def cut_rod(p, n, mem):
	ans = 0
	if n in mem: ans = mem[n]
	else:
		if n > 0:
			ans = INF
			i = 0
			while i!=n :
				ans = max(ans, p[i] + cut_rod(p, n-i-1, mem))
				i += 1
		mem[n] = ans
	return ans

l = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(cut_rod(l, len(l), mem))

def tab_cut_rod(p, n):
	r = [INF for _ in range(n+1)]
	r[0] = 0
	i = 1 
	while i != n+1:
		q = INF
		j = 0
		while j != i:
			q = max(q, p[j] + r[i-j-1])
			j += 1
		r[i] = q
		i += 1
	return r[n]

print(tab_cut_rod(l,len(l)))
