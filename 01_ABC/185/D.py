

if __name__ == '__main__':
    N, M = map(int, input().split())
    if M == 0:
        print(1)
    else:
        A = [0]
        A += list(map(int, input().split()))
        A.sort()
        A.append(N+1)
        k = N+1
        for i in range(1, M+2):
            if A[i]-A[i-1] > 1:
                k = min(k, A[i]-A[i-1]-1)

        ans = 0
        for i in range(1, M+2):
            if (A[i]-A[i-1]-1) % k == 0:
                ans += (A[i]-A[i-1]-1) // k
            else:
                ans += (A[i]-A[i-1]-1) // k + 1

        print(ans)


