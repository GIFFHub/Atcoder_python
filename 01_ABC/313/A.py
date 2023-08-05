

if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))
    if N == 1:
        print(0)
    else:
        max_P = max(P[1:])
        if max_P >= P[0]:
            print(max_P - P[0] + 1)
        else:
            print(0)

