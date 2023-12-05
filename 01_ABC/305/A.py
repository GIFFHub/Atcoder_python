

if __name__ == '__main__':
    N = int(input())

    P = N//5

    back = N-P*5
    front = (P+1)*5 - N

    if back < front:
        print(N-back)
    else:
        print(N+front)
