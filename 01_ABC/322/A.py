

if __name__ == '__main__':
    N = int(input())
    S = input()

    for i in range(N):
        if i <= N-3:
            if S[i:i+3] == 'ABC':
                print(i+1)
                break
    else:
        print(-1)