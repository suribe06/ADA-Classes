
#phi(low,hi) = 1 + phi(low+1, hi -1)             , comp(A[low], A[hi-1]). = true

#              max(phi(low+1,hi), phi(low,hi-1)) , comp(A[low], A[hi-1]). = false


def phi(A, low, hi):
    assert 0 <= low <= hi <= len(A)
    ans = None
    if hi - low <= 4: ans = 0
    else:
        if comp(A[low], A[hi-1]):
            ans = 1 + phi(A, low+1, hi-1)
        else:
            ans = max(phi(A, low+1, hi), phi(A, low, hi-1))
    return ans

def comp(b1, b2):
    ans = None
    if (b1 == 'A' and b2 == 'U') or (b1 == 'U' and b2 == 'A') or (b1 == 'C' and b2 == 'G') or (b1 == 'G' and b2 == 'C'):
        ans = True
    return ans


def tab_phi(A):
    N = len(A)
    tab = [[0 for _ in range(N+1)] for _ in range(N+1)]
    low, hi = N-5, N
    while low >= 0:
        if hi == N+1:
            low -= 1
            hi = low + 5
        else:
            if comp(A[low], A[hi-1]) == True: tab[low][hi] = 1 + tab[low+1][hi-1]
            else:
                tab[low][hi] = max(tab[low+1][hi], tab[low][hi-1])
                hi += 1
    return tab[0][N]

A = ['A', 'C', 'A', 'U', 'G', 'A', 'U', 'G', 'G', 'C', 'C', 'A', 'U', 'G', 'U']

#print(phi(A, 0, len(A)))
#print(tab_phi(A))
