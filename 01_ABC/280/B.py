

if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))
    A = [S[0]]
    for i in range(N-1):
        A.append(S[i+1]-S[i])

    print(*A)
