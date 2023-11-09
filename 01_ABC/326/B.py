

if __name__ == '__main__':
    N = int(input())
    tmp = N
    while True:
        S = str(tmp)
        h = int(S[0])
        m = int(S[1])
        s = int(S[2])
        if h*m == s:
            print(S)
            break
        tmp += 1
