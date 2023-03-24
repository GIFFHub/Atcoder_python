import bisect

if __name__ == '__main__':

    S = input()
    N = len(S)
    point = []
    for i in range(N-1):
        if S[i] == 'R' and S[i+1] == 'L':
            point.append(i)

    ans = [0]*N
    for i, s in enumerate(S):
        terminal = bisect.bisect_left(point, i)
        if s == 'L':
            terminal -= 1
        move = abs(point[terminal] - i)
        ans[point[terminal] + move % 2] += 1
    print(*ans)


