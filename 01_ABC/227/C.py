import math

if __name__ == '__main__':
    N = int(input())

    ans = 0
    for A in range(1, N):
        if A > math.pow(N, (1/3)):
            break
        for B in range(1, N):
            if B > math.pow(N, (1/2)):
                break
            C_max = N//(A*B)
            ans += C_max - B + 1

    print(ans)
