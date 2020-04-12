all_sols = []

def subset_sum(A, n, N, x, psol):
    global all_sols
    if n == N:
        if x == 0:
            all_sols.append(list(psol))
    else:
        subset_sum(A, n+1, N, x, psol) #ignoro
        if A[n] <= x: #agrego
            psol.append(A[n])
            subset_sum(A, n+1, N, x-A[n], psol)
            psol.pop()

A = [1, 4, 1, 3, 2]
N = len(A)

subset_sum(A, 0, N, 5, [])

print(all_sols)
