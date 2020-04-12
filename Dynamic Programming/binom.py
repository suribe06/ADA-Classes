def binom(n, k, memo):
  assert 0 <= k <= n
  ans,key = None,(n, k)
  if key in memo: ans = memo[key]
  else:
    if k==0 or k==n: ans = 1
    else:
      if n<(k<<1): k = n-k
      ans = binom(n-1, k-1, memo) + binom(n-1, k, memo)
    memo[key] = ans
  return ans

def binom_tab(N, K):
    tab = [ [ 0 for _ in range(K+2) ] for _ in range(N+2) ]
    for i in range(N+1):
      for j in range(K+1):
          tab[i][0] = 1
          if i == j:
              tab[i][j] = 1

    n, k = 1, 0
    while n != N+1:
      if k == K+1:
         n, k = n+1, 0
      else:
          tab[n][k] = tab[n-1][k-1] + tab[n-1][k]
          k += 1

    return tab[N][K]

def imprimirMatriz(tab, N, K):
    a=""
    for k in range(N+1):
        for j in range(K+1):
            a+=str(tab[k][j])+'\t'
        print (a)
        a=""

memo = dict()
print(binom(36, 6, memo)) #792
#print(binom_tab(12, 5)) #792
