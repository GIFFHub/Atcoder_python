

if __name__ == '__main__':
    A, B = map(float, input().split())

    B = str(B)
    index = B.find('.')
    front = B[:index]
    back = B[index+1:]
    while len(back) < 2:
        back += '0'
    B = front + back
    flg = 1
    T = []
    for b in B:
        if flg:
            if b == 0:
                continue
            else:
                flg = 0
        T.append(b)

    B = ''.join(T)
    B = int(B)
    A = int(A)
    tmp = 0
    for i in range(B):
        tmp += A
    tmp = str(tmp)
    if len(tmp) < 3:
        print(0)
    else:
        print(tmp[:-2])
