from collections import deque


if __name__ == '__main__':
    # input
    N = int(input())
    S = input()
    A = [0]
    A_left = deque()
    A_right = deque()

    index = 0
    for i in range(1, N+1):
        if S[i-1] == 'L':
            A_right.appendleft(i-1)
        else:
            A_left.append(i-1)
    if len(A_left) > 0:
        print(*A_left, end= ' ')
    print(i, end=' ')

    if len(A_right) > 0:
        print(*A_right)