

if __name__ == '__main__':
    W, H, x, y = map(int, input().split())

    S = W*H/2
    t = 0
    if x*2 == W and y*2 == H:
        t = 1

    print(S, t)
