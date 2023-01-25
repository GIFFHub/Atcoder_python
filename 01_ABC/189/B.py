

if __name__ == '__main__':
    N, X = map(int, input().split())
    X *= 100
    alc = 0
    for i in range(N):
        v, p = map(int, input().split())
        alc += v*p
        if alc > X:
            print(i+1)
            break
    else:
        print(-1)



