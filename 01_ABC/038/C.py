

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    R = [None]*N
    ans = 0
    for i in range(N):
        if i == 0:
            R[0] = 0
        else:
            # R[i]は最も小さくてもi始まりであるはず
            R[i] = max(i, R[i-1])

        # R[i]まではいける前提。
        # R[i]+1がいけなくなるまでwhileループ
        # →　R[i]がぎりぎりいけるラインになる
        while R[i]+1 < N and A[R[i]] < A[R[i]+1]:
            R[i] += 1

        ans += R[i]-i+1

    print(ans)