

if __name__ == '__main__':
    N = int(input())
    H = list(map(int, input().split()))

    H_max = max(H)
    print(H.index(H_max)+1)