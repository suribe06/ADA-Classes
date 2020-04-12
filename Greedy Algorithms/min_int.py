
def minimal_covering(L, H, l, h):
    ans, low, n = list(), L, 0
    N = len(l)
    while low < H and n != N:              #P1, P2 and P3
        best, n = n, n+1
        while n != N and l[n] <= low:      #P0 and P1
            if h[n] > h[best]:
                best = n
            n+=1
        ans.append(best)
        low = h[best]
    return ans

"""
P0: h[best] = (max i | 0<=i<n and l[best]<=low<=h[best])
P1: 0 <= n <= N
P2: l <= low
P3: [L, low] contenido en la union [l[b[i]], h[b[i]]] for 0<=i<=len(b)
"""

def minimal_covering_with_failure(L, H, l, h):
    ans, low, n, ok = list(), L, 0, True
    N = len(l)
    while ok and low < H and n != N:
        ok = l[n] <= low and low <= h[n]
        best, n = n, n+1
        while ok and n != N and l[n] <= low:
            if h[n] > h[best]:
                best = n
            n+=1
        ans.append(best)
        low = h[best]
    ok = ok and low >= H
    if ok == False:
        ans = list()
    return ans

def minimal_covering_with_failure_2(L, H, s):
    ans, low, n, ok = list(), L, 0, True
    N = len(s)
    while ok and low < H and n != N:
        ok = s[n][0] <= low and low <= s[n][1]
        best, n = n, n+1
        while ok and n != N and s[n][0] <= low:
            if s[n][1] > s[best][1]:
                best = n
            n+=1
        ans.append(best)
        low = s[best][1]
    ok = ok and low >= H
    if ok == False:
        ans = list()
    return ans, ok

#l = [0, 0, 10, 20, 30]
#h = [10, 20, 30, 40, 40]

#l = [0, 8, 15]
#h = [20, 28, 35]

#s = [(0,10), (10,30), (30,40)]
#s = [(0, 20), (8, 28), (15,35)]
s = [(0,10), (20,40)]

#l = [0, 10, 30]
#h = [10, 30, 40]

print(minimal_covering_with_failure_2(0, 40, s))
