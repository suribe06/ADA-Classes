
def phi(A, n, x):
    ans = None
    if n == 0: ans = x == 0
    else:
        if A[n-1] > x:
            ans = phi(A, n-1, x)
        else:
            ans = phi(A, n-1, x) or phi(A, n-1, x-A[n-1])
    return ans

def ssum(A, n, x): #rochin
    ans = None
    if n == 0: ans = x == 0
    else:
        ans = ssum(A, n-1, x)
        if ans != True and A[n-1] <= x:
            ans = ssum(A, n-1, x-A[n-1])

    return ans

def phi_memo(A, n, x, memo):
    ans, key = None, (n, x)
    if key in memo: ans = memo[key]
    else:
        if n == 0: ans = x == 0
        else:
            if A[n-1] > x:
                ans = phi_memo(A, n-1, x, memo)
            else:
                ans = phi_memo(A, n-1, x, memo) or phi_memo(A, n-1, x-A[n-1], memo)
        memo[key] = ans
    return ans

def ssum_tab(A, X):
    N = len(A)
    tab = [ [ False for _ in range(X+1) ] for _ in range(N+1) ]
    tab[0][0] = True
    n, x = 1, 0
    while n != N+1:
        if x == X+1:
            n, x = n+1, 0
        else:
            if A[n-1] > x:
                tab[n][x] = tab[n-1][x]
            else:
                tab[n][x] = tab[n-1][x] or tab[n-1][x-A[n-1]]
            x += 1
    return tab[N][X]

memo = dict()
A = [3, 0, 1, 7, 10, 6, 7]

#print(phi(A, len(A), 4))
print(phi_memo(A, len(A), 4, memo))
#print(ssum_tab(A, 4))
