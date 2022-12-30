from collections import deque

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    D = deque()
    balls = 0

    for i in range(N):
        if len(D) == 0:
            D.append([A[i], 1])
            balls += 1

        elif D[-1][0] == A[i]:
            D[-1][1] += 1
            balls += 1
            if D[-1][0] == D[-1][1]:
                balls -= D.pop()[1]

        else:
            D.append([A[i], 1])
            balls += 1

        print(balls)




