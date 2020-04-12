def merge(A,B):
    c = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1

    c += A[i:]
    c += B[j:]
    return c

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) >> 1
        a = mergesort(arr[:mid])
        b = mergesort(arr[mid:])
        return merge(a,b)

A = [10, 2, 5, 1, 7, 4, 9]

print(mergesort(A))
