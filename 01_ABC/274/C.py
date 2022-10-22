N = int(input())
A = list(map(int, input().split()))

ans = [0]*(2*N+1)
for i in range(N):
    # A[i] のところから、2i と2i+1の子ができる
    # 2i と 2i+1 の子のレベルを親＋１に設定する
    ans[2*(i+1)-1] = ans[A[i]-1] + 1
    ans[2*(i+1)] = ans[A[i]-1] + 1


for x in ans:
    print(x)
