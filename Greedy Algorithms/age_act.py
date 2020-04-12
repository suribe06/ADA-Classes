
def act_sech(s, f):
    ans, n = 0, 0
    N = len(s)
    while n != N:
        best, n = n, n+1
        while n != N ans s[n] < f[best]:
            n+=1
        ans += 1
    return ans

"""
P0: f[best] = (min i | best<=i<N: f[i])
P1: 0<=n<=N
P2: (for all i | best<=i<n: s[n] < f[best])
P3: ans = phi(0,n)
Cmplejidad O(n) si la entrada esta ordenada, si no O(nlog(n))
"""


def act_sch(a):
  a.sort(key=lambda x : x[1])  # sort activities by earliest finish time
  ans,n,N = 0,0,len(a)
  while n != N:
    best,n,ans = n,n+1,ans+1
    while n!=N and a[n][0]<a[best][1]:
      n += 1
  return ans
