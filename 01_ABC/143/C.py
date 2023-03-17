

if __name__ == '__main__':
    N = int(input())
    S = input()

    for i in range(1, N):
        if S[i] == S[i-1]:
            N -= 1

    print(N)
