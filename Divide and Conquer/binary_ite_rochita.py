def binary_search_ite(A, x):
	N = len(A)
	ans = None
	if N > 0:
		low, hi = 0, N
		while low + 1 != hi:
			mid = low + ((hi - low) >> 1)
			if x < A[mid]:
				hi = mid
			else:
				low = mid
		ans = A[low] == x
	return ans, low

A = [1,2,3,4,5,6]

print(binary_search_ite(A, 8))
