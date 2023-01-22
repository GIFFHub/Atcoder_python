

if __name__ == '__main__':
    N = int(input())
    A = input()
    B = input()
    T = 998244353
    tmp1 = []
    tmp2 = []
    for i in range(N):
        tmp1.append(max(A[i], B[i]))
        tmp2.append(min(A[i], B[i]))

    A2 = ''.join(tmp1)
    B2 = ''.join(tmp2)
    A2 = int(A2)
    B2 = int(B2)

    ans = A2*B2 % 998244353

    print(ans)







