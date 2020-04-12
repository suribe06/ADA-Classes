def fibonacci(n):
    assert n >= 0
    ans = None
    if n <= 1:
        ans = n
    else:
        ans = fibonacci(n-2) + fibonacci(n-1)
    return ans

def fibonacci_memo(n, mem):
    ans = None
    if n in mem: ans= mem[n]
    else:
        if n <= 1:
            ans = n
        else:
            ans = fibonacci_memo(n-2, mem) + fibonacci_memo(n-1, mem)
        mem[n] = ans
    return ans

def main():
    m = dict()
    r = fibonacci_memo(50, m)
    print(r)

main()
