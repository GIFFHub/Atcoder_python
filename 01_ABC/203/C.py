import bisect

if __name__ == '__main__':
    N, K = map(int, input().split())
    money = K
    friends = []
    T = 10**100+1
    for _ in range(N):
        a, b = map(int, input().split())
        friends.append((a, b))

    friends.sort(key=lambda x: x[0])
    A = []
    B = []
    for f in friends:
        A.append(f[0])
        B.append(f[1])
    B_crr = [0]
    tmp = 0
    for i in range(N):
        tmp += B[i]
        B_crr.append(tmp)

    villa = 0
    prev = 0
    # まず所持金だけ進む。その後通った村でもらったお金再計算する。
    while True:
        villa += money
        money = 0
        if villa > T:
            villa = T
            break

        friends_num = bisect.bisect_right(A, villa)
        money += B_crr[friends_num] - B_crr[prev]
        prev = friends_num

        if money <= 0:
            break

    print(villa)








