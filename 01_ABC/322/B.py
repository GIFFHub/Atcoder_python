

if __name__ == '__main__':

    N, M = map(int, input().split())
    S = input()
    T = input()

    if T[:N] == S:
        if T[-N:] == S:
            print(0)
        else:
            print(1)
    else:
        if T[-N:] == S:
            print(2)
        else:
            print(3)
