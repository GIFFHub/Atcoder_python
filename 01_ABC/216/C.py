from collections import deque

if __name__ == '__main__':
    N = int(input())
    ans = deque()
    while True:
        if N == 0:
            break

        if N % 2 == 0:
            N //= 2
            ans.appendleft('B')
        else:
            N -= 1
            ans.appendleft('A')

    print(''.join(ans))



