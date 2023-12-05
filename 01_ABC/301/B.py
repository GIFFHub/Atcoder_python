

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    ans = []
    for i in range(N-1):
        ans.append(A[i])
        if A[i] < A[i+1]:
            tmp = A[i]
            while True:
                tmp += 1
                if tmp == A[i+1]:
                    break
                else:
                    ans.append(tmp)
        else:
            tmp = A[i]
            while True:
                tmp -= 1
                if tmp == A[i+1]:
                    break
                else:
                    ans.append(tmp)
    ans.append(A[-1])
    print(*ans)