

if __name__ == '__main__':

    N = int(input())
    P = list(map(int, input().split()))

    cnt = [0] * N # 各操作回数による喜ぶ人の数（加算していく）

    for i in range(N): # それぞれの料理に対して喜ぶ操作回数を調査
        # 料理（P[i]）を人（P[i]-1）の人の前に持っていくための操作回数
        cnt[(P[i-1]-i) % N] += 1
        cnt[(P[i]-i) % N] += 1
        cnt[(P[(i+1)%N]-i) % N] += 1

    print(max(cnt))
