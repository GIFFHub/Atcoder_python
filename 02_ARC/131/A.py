

if __name__ == '__main__':
    A = input()
    B = int(input())

    '''
    考察
    ・前半の８桁はAにして、後半の９桁はBの半分にすれば？
    
    '''

    front = '0'*(8-len(A))+A

    if B % 2 == 0:
        B //= 2
        back = '0'*(8-len(str(B)))+str(B)
    else:
        B -= 1
        B //= 2
        back = '0'*(7-len(str(B)))+str(B)+'5'

    ans = ''
    flg = True
    for b in (front+back):
        if flg:
            if b == '0':
                pass
            else:
                ans += b
                flg = False
        else:
            ans += b
    print(ans)