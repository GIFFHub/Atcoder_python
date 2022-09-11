from collections import deque


def count_next(a):
    a = list(a)
    cnt = 0
    for j in range(len(a)):
        tmp = a[j] - j
        if tmp == 0 or tmp == 1 or tmp == -1 or tmp == N-1 or tmp == 1-N:
            cnt += 1
        if cnt == 5:
            pass
    return cnt


if __name__ == '__main__':
    N = int(input())
    P = deque(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        P.rotate(i)
        ans = max(ans, count_next(P))
        if ans == N:
            break
    print(ans)



