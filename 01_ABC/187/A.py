

if __name__ == '__main__':
    A, B = input().split()
    S = [0, 0]
    tmp = 0
    for a in A:
        tmp += int(a)
    S[0] = tmp
    tmp = 0
    for b in B:
        tmp += int(b)
    S[1] = tmp

    print(max(S))

