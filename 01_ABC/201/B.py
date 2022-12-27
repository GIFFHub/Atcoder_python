

if __name__ == '__main__':
    N = int(input())
    S = []
    T = []
    K = []
    for _ in range(N):
        s, t = input().split()

        S.append(s)
        T.append(int(t))
        K.append((s,int(t)))

    K.sort(key=lambda x: x[1], reverse=True)

    print(K[1][0])
