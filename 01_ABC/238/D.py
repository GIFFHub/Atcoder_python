def check_bit(b: int, k: int) -> bool:
    '''
    :param b: 判定する2進数
    :param k: 後ろからk番目
    :return: bについて後ろからk番目のbitが立っているか
    '''
    if b & (1 << k):
        return True
    else:
        return False


if __name__ == '__main__':
    # input
    T = int(input())
    for _ in range(T):
        # input
        a, s = map(int, input().split())
        # sの2進数bit数
        len_a = len(bin(a))-2
        len_s = len(bin(s))-2

        if a == 1:
            if not check_bit(s, 0):
                print('Yes')
                continue

        if a == 0:
            print('Yes')
            continue

        if a == s:
            print('No')
            continue

        if len_a >= len_s:
            print('No')
            continue
        # check
        tmp = 0  # 繰り上がり桁数

        for i in range(len_s):
            # aのi桁目が1の場合:(1,1)
            if check_bit(a, i):

                # 繰り上がりなしで,sのi桁目が1
                # → xかs-xのi桁目:(0,1) or (1,0)
                # → aのi桁目が1にならないのでありえない
                if check_bit(s, i) and tmp == 0:
                    # xとs-xが両方
                    print('No')
                    break

                # 繰り上がりありで,sのi桁目が1
                # → xかs-xのi桁目が(0,0) or (1,1)
                # aのi桁目が1なので、(1,1)のみありえる→繰り上がりありのまま
                elif check_bit(s, i) and tmp == 1:
                    pass

                # 繰り上がりなしで,sのi桁目が0
                # → xとs-xのi桁目が両方1 ならありえる
                elif (not check_bit(s, i)) and tmp == 0:
                    # xとs-xのi桁目が両方1なので繰り上がり
                    tmp = 1

                # 繰り上がりありで,sのi桁目が0
                # → xかs-xのi桁目が(0,1) or (1,0)でないといけないが
                # x と s-x は (1,1)でないといけないのでout
                elif (not check_bit(s, i)) and tmp == 1:
                    print('No')
                    break

            # aのi桁目が0の場合：(0,1) or (1,0) or (0,0)
            else:
                # 繰り上がりなしで,sのi桁目が1
                # → xかs-xのi桁目が(0,1) or (1,0)→ありえる
                if check_bit(s, i) and tmp == 0:
                    pass

                # 繰り上がりありで,sのi桁目が1
                # → xかs-xのi桁目が(0,0) or (1,1) → (0,0)のみありえる
                elif check_bit(s, i) and tmp == 1:
                    tmp = 0

                # 繰り上がりなしで,sのi桁目が0
                # → xとs-xのi桁目が(0,0) or (1,1) →(0,0)のみありえる
                elif (not check_bit(s, i)) and tmp == 0:
                    pass

                # 繰り上がりありで,sのi桁目が0
                # → xかs-xのi桁目が(0,1) or (1,0) → そのまま繰り上がり
                elif (not check_bit(s, i)) and tmp == 1:
                    pass
        else:
            print('Yes')
