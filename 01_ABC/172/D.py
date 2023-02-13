
if __name__ == '__main__':
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N//i+1):
            ans += i*j

    print(ans)