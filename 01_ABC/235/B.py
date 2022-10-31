

if __name__ == '__main__':
    N = int(input())
    H = list(map(int, input().split()))

    pos = 0
    for i in range(1, N):
        if H[i] > H[i-1]:
            pos = i
        else:
            break

    print(H[pos])
