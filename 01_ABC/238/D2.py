import sys

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        a = bin(a)[2:].zfill(60)
        s = bin(s)[2:].zfill(60)
        ans = 'Yes'
        flg = 0 # 繰り上がり
        for i in range(1, 61):
            a_tmp = a[-i]
            s_tmp = s[-i]
            # and:0 (x,y) = (0,0) or (0,1) or (1,0)
            if a[-i] == '0':
                # or:0 (x,y) = 繰り上がりなし：(0,0) or ×(1,1) あり（1,0) or (0,1)
                if s[-i] == '0':
                    if flg:
                        flg = 1
                    else:
                        flg = 0
                # or:1 (x,y) = 繰り上がりなし:(0,1) or (1,0) or あり(0,0) or ×(1,1)
                else:
                    if flg:
                        flg = 0
                    else:
                        flg = 0
            # and:1 (x,y) = (1,1)
            else:
                # or:0 (x,y) = 繰り上がりなし：(1,1) or ×(0,0)　繰り上がりあり：×(0,1) or ×(1,0)
                if s[-i] == '0':
                    if flg:
                        break
                    else:
                        flg = 1
                # or:1 (x,y) = 繰り上がりなし：×(0,1) or ×(1,0)繰り上がりあり：×(0,0) or (1,1)
                else:
                    if flg:
                        flg = 1
                    else:
                        flg = 1
                        break
        if flg:
            print('No')
        else:
            print('Yes')






