

if __name__ == '__main__':
    H, A = map(int, input().split())
    if H % A == 0:
        ans = H // A
    else:
        ans = H // A + 1

    print(ans)