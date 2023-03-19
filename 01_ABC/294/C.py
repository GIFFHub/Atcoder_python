

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = A+B
    C.sort()
    a = 0
    b = 0
    A_ans = []
    B_ans = []
    for i, c in enumerate(C):
        if a < N:
            if c == A[a]:
                A_ans.append(i+1)
                a += 1
            else:
                B_ans.append(i+1)
                b += 1
        else:
            B_ans.append(i+1)

    print(*A_ans)
    print(*B_ans)
