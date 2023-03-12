

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 1
    break_num = 0
    for i in range(N):
        if A[i] == cnt:
            cnt += 1
        else:
            break_num += 1
    if cnt == 1:
        print(-1)
    else:
        print(break_num)
