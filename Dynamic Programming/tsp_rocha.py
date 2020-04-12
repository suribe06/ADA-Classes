INF = float('inf')
n, memo = 5, dict()

def tsp_fb(v, A, vs):
  ans = INF
  if A == (1<<n) - 1:
    ans = adj[v][vs]
  else:
    for i in range(n):
      if i != v and (A & (1<<i)) == 0:
        ans = min(ans, adj[v][i] + tsp_fb(i, (A | (1<<i)), vs))
  return ans

def tsp_dp(v, A, vs):
  global memo
  ans = INF
  if (v,A) in memo:
    ans = memo[(v,A)]
  else:
    if A == (1<<n) - 1:
      ans = adj[v][vs]
    else:
      for i in range(n):
        if i != v and (A & (1<<i)) == 0:
          ans = min(ans, adj[v][i] + tsp_dp(i, (A | (1<<i)), vs))
    memo[(v,A)] = ans
  return ans


