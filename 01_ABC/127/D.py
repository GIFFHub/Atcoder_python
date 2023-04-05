from collections import defaultdict

if __name__ == '__main__':
    N, M = input().split()
    A = list(map(int, input().split()))
    K = []
    for j in range(M):
        B, C = map(int, input().split())
        K.append([B, C])

    A.sort(reverse=True)
    d = defaultdict(int)
    for a in A:
        d[a] += 1

    A_set = set(A)
    A_set_list = list(A_set)
    A_set_list.sort()
    T = []
    for a_s in A_set_list:
        T.append([d[a_s], a_s])

    K = sorted(K, key=lambda x : x[1], reverse=True)

    cnt = 0
    ans = 0
    len_T0 = len(T)
    for j in range(M):
        # 今回何枚変えられるか
        b = K[j][0]
        # 今回何に変えられるか
        c = K[j][1]
        # 今回変えられる値よりも、既存の最大値の方が小さい場合
        while cnt < len_T0:
            if T[cnt][1] < c:
                while b > 0:
                    if T[cnt][1] < c:
                        # 今回変えられる枚数より、最大値（変える対象）の枚数の方が多い場合、
                        if T[cnt][0] > b:
                            T[cnt][0] -= b
                            ans += b*c
                            b = 0
                        # 今回変えられる枚数の方が、最大値（変える対象）の枚数より多い場合、
                        else:
                            b -= T[cnt][0]
                            ans += T[cnt][0]*c
                            cnt += 1
                    else:
                        break
                break
            else:
                break

    for x in range(cnt, len_T0):
        ans += T[x][1]*T[x][0]

    print(ans)









