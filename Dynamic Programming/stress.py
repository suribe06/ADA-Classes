
def stress(Ls,Hs,n,mem):
	ans = None
	if n in mem: ans = mem[n]
	else:
		if(n==0):
			ans = 0
		if(n==1):
			ans = max(Ls[0],Hs[0])
		else:
			ans = max((Ls[n-1] + stress(Ls,Hs,n-1,mem)),(Hs[n-1] + stress(Ls,Hs, n-2,mem)), stress(Ls,Hs,n-1,mem))
		mem[n] = ans
	return ans 

def stressT(Ls,Hs):
	N = len(Ls)
	tab = [[0 for _ in range(N+1)] for _ in range(N+1)]
	tab[0] = 0
	tab[1] = max(Ls[0],Hs[0])
	for n in range(2,N+1):
		tab[n] = max((Ls[n-1]+tab[n-1]), Hs[n-1] + tab[n-2], tab[n-1])
	return tab[N]

def stressTO(Ls,Hs):
	n = len(Ls)
	a = 0
	b = max(Ls[0],Hs[0])
	for i in range(2,N+1):
		a,b = max((Ls[n-1]+b), Hs[n-1] + a, b)
	return b

def main():
main()