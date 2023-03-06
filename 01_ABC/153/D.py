from collections import deque

if __name__ == '__main__':
    H = int(input())
    cnt = 0
    while H > 0:
        cnt += 1
        H //= 2

    ans = 1
    for i in range(1, cnt):
        ans += 2**i

    print(ans)





