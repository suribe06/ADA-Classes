#Entrada: A[0..N) DE CARACTERES
#Salida: # de enlaces posibles

#   0.  hi-low <= 4

#phi(low,hi) = 1 + phi(low+1, hi -1)             , comp(A[low], A[hi-1]). = true

#              max(phi(low+1,hi), phi(low,hi-1)) , comp(A[low], A[hi-1]). = false 

def comp(b1,b2):
	return (b1 == 'A' and b2 == 'U') or (b1 == 'U' and b2 == 'A') or (b1 == 'G' and b2 == 'C')

def adn(A,low,hi,mem):
	assert 0<=low<=hi
	ans = None
	if (low,hi) in mem : ans = mem[(low,hi)]
	else:
		if(hi-low <= 4): ans = 0
		else:
			if(comp(A[low], A[hi-1]) == True): ans = 1+adn(A,low+1,hi-1,mem)
			else:
				ans = max(adn(A,low+1,hi,mem),adn(A,low,hi-1,mem))
		mem[(low,hi)] = ans
	return ans


def adnTab(A):
	n = len(A)
	tab = [[0 for _ in range(n+1)] for _ in range(n+1)]
	low,hi = n-5, n
	while(low>=0):
		if(hi==n+1):
			low-=1
			hi=low+5
		else:
			if(comp(A[low], A[hi-1]) == true):  tab[low][hi] = 1+tab[low+1][hi-1]
			else:
				tab[low][hi] = max(tab[low+1][hi],tab[low][hi-1])
				hi+=1
	return tab[0][n]

def main():
	A = ['A', 'C', 'A', 'U', 'G', 'A', 'U', 'G', 'G', 'C', 'C', 'A', 'U', 'G', 'U']
	mem = dict()
	print(adn(A, 0, len(A)-1, mem))
main()
