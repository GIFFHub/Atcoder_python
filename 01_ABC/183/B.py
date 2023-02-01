

if __name__ == '__main__':
    Sx, Sy, Gx, Gy = map(int, input().split())

    ans = ((Sy*Gx) + (Sx*Gy)) / (Sy+Gy)

    print(ans)