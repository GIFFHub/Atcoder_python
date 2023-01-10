

if __name__ == '__main__':
    N, X = map(int, input().split())
    A = []
    B = []
    tmp_min = 10**9+1
    tmp_time = 0
    ans = 2*(10**18)+1

    for i in range(1, N+1):
        a, b = map(int, input().split())
        if i <= X:
            tmp_time += (a+b)
            tmp_min = min(tmp_min, b)
            ans = min(ans, tmp_time + b*(X-i))

    print(ans)








