

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    T = dict()
    for _ in range(M):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        if a in T:
            T[a].append((b, c))
        else:
            T[a] = [(b, c)]

    '''
    f(s,t,k) : sからtまでk以下の都市のみを通る最短時間
    
    f(s,t,k+1)を考える
    　・k+1ルートを使わない場合は、f(s,t,k)と同じになる
    　・k+1ルートを使う場合
    　　k+1ルートを必ず通るため、f(s,k+1,k) + f(k+1,t,k)になる
    
    よってf(s,t,k+1) = min(f(s,t,k), f(s,k+1,k)+f(k+1,t,k))
    
    あらかじめ求めておくのは以下
    f(1,*,1)
    f(*,1,1)    
    '''
    ans = 0
    f = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for s in range(N):
        for t in range(N):
            for k in range(N-1):
                f[s][t][k+1] = min(f[s][t][k], f[s][k+1][k] + f[k+1][t][k])
                ans += f[s][t][k+1]
    print(f)

