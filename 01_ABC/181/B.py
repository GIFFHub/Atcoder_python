

if  __name__ == '__main__':
    N = int(input())
    ans = 0
    for _ in range(N):
        a, b = map(int, input().split())
        S = (a+b)*(b-a+1)//2
        ans += S

    print(ans)
