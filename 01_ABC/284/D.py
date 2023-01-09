import math

if __name__ == '__main__':
    T = int(input())
    p = 0
    q = 0
    for _ in range(T):
        N = int(input())
        M = math.pow(N, 1/3)
        M = round(M)
        for i in range(2, M+1):
            if N % i == 0:
                N //= i
                if N % i == 0:
                    p = i
                    q = N//i
                else:
                    q = i
                    p = math.pow(N, 1/2)
                break
        print(int(p), q)


