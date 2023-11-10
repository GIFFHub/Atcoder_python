from collections import defaultdict

if __name__ == '__main__':
    # 初期化
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = []
    for _ in range(N):
        S.append(input())

    d = defaultdict(int)
    max_point = 0
    points = []
    for i in range(N):
        point = i+1
        for j in range(M):
            if S[i][j] == 'o':
                point += A[j]
        points.append(point)
        d[point] += 1
        max_point = max(point, max_point)

    A_sort = []
    for k in range(M):
        A_sort.append((A[k], k))
    A_sort.sort(reverse=True)

    for l in range(N):
        cnt = 0
        # 現時点で最高得点の場合
        if points[l] == max_point:
            # 同点がいない場合
            if d[max_point] == 1:
                print(0)
            # 同点がいる場合
            else:
                print(1)
        # 現時点で最高得点ではない場合
        else:
            tmp_point = points[l]
            for m in range(M):
                # 加点候補の問題
                check_q = A_sort[m][1]
                # 加点候補の問題が既に解答済みの場合
                if S[l][check_q] == 'o':
                    continue
                # まだ解いていない場合
                else:
                    # 加点する
                    tmp_point += A_sort[m][0]
                    cnt += 1
                    if tmp_point > max_point:
                        print(cnt)
                        break








