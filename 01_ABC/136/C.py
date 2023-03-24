

if __name__ == '__main__':
    N = int(input())
    H = list(map(int, input().split()))
    H.reverse()
    for i in range(N-1):
        if H[i] < H[i+1]:
            if H[i+1] - H[i] == 1:
                H[i+1] -= 1
            else:
                break
    else:
        print('Yes')
        exit()
    print('No')