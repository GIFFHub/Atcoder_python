

if __name__ == '__main__':

    N = int(input())
    ans = 0
    for i in range(N):
        x, u = input().split()
        if u == 'JPY':
            x = int(x)
            ans += x
        else:
            x = float(x)
            ans += 380000*x
    print(ans)