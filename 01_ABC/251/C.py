def judge(index):
    # S_set = set(S[:best_index])
    if S[best_index] in S[:best_index]:
        return False
    else:
        return True


if __name__ == '__main__':

    # 入力
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))


    while True:
        # 暫定１位のインデックス
        best_index = T.index(max(T))
        if judge(best_index):
            print(best_index+1)
            break
        else:
            T[best_index] = 0
            S[best_index] = False





