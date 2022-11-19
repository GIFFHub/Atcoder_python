def check(a, b, c, d):
    if int(str(a)+str(c)) < 24 and int(str(b)+str(d)) < 60:
        return True
    else:
        return False


if __name__ == '__main__':
    H, M = input().split()

    if len(H) == 2:
        A = int(H[0])
        B = int(H[1])
    else:
        A = 0
        B = int(H[0])

    if len(M) == 2:
        C = int(M[0])
        D = int(M[1])
    else:
        C = 0
        D = int(M[0])

    while True:
        if check(A, B, C, D):
            print(str(A)+str(B), str(C)+str(D))
            break

        D += 1
        if D >= 10:
            D = 0
            C += 1
            if C >= 6:
                C = 0
                B += 1
                if B >= 10:
                    B = 0
                    A += 1
                    if A >= 3:
                        A = 0
                elif B >= 4 and A == 2:
                    B = 0
                    A = 0

