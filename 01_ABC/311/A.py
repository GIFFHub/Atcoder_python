

if __name__ == '__main__':
    N = int(input())
    S = input()
    K = set()
    cnt = 0
    for s in S:
        cnt += 1
        K.add(s)
        if len(K) == 3:
            print(cnt)
            break