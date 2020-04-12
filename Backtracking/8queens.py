from sys import setrecursionlimit
setrecursionlimit(100000)

all_sols = list()

def safe(A, n, r):
    ans, c = True, 0
    while ans and c != n:
        ans = A[c] != r and n-c != r-A[c] and n-c != A[c]-r #conflicto fila, conflicto diagonal arriba, conflicto diagonal abajo
        c += 1
    return ans

def queens(A, n):
    global all_sols
    assert 0 <= n <= 8
    if n == 8:
        all_sols.append(list(A))
    else:
        for r in range(8):
            if safe(A, n, r):
                A[n] = r
                queens(A, n+1)

A = [None for _ in range(8)]
queens(A, 0)
"""for x in all_sols:
    print(x)"""
print(len(all_sols))
