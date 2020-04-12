

def phi(A, low, hi):
    assert 0 <= low and hi <= len(A)
    ans = None
    if low > hi: ans = 0
    elif low == hi: ans = 1
    else:
        if comp(A[low], A[hi]):
            ans = 2 + phi(A, low+1, hi-1)
        else:
            ans = max(phi(A, low+1, hi), phi(A, low, hi-1))
    return ans

def comp(b1, b2):
    return b1 == b2

def phi_tab(A):
    N = len(A)
    tab = [[0 for _ in range(N+1)] for _ in range(N+1)]

    
    return tab[0][N]

A = ['A', 'B', 'B', 'D', 'C', 'A', 'C', 'B']
low = 0
hi = len(A)
print(phi(A, low, hi-1))
