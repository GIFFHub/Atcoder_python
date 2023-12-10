if __name__ == '__main__':
    K, G, M = map(int, input().split())

    glass = 0
    mag = 0
    for i in range(K):
        if glass == G:
            glass = 0
        elif mag == 0:
            mag = M
        else:
            rest_glass = G-glass
            if rest_glass > mag:
                glass += mag
                mag = 0

            else:
                glass = G
                mag -= rest_glass
            rest_glass = 0

    print(glass, mag)
