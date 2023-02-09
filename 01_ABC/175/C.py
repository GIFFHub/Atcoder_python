

if __name__ == '__main__':
    X, K, D = map(int, input().split())
    '''
    ・とりあえず座標0まで行く
    ・原点跨いだらまたぐの繰り返し
    
    '''

    # 原点まで何回でたどり着くか
    first_num = abs(X) // D # あと1回で原点にたどり着くような移動回数
    # 原点まで行かない場合
    if first_num >= K:
        if X > 0:
            ans = abs(X - K*D)
        else:
            ans = abs(X + K*D)
    # 原点直前までは行く場合
    else:
        if X > 0:
            first_point = X - D*first_num
            second_point = X - D*(first_num+1)
            if first_num % 2 == K % 2:
                ans = abs(first_point)
            else:
                ans = abs(second_point)
        else:
            first_point = X + D*first_num
            second_point = X + D*(first_num+1)
            if first_num % 2 == K % 2:
                ans = abs(first_point)
            else:
                ans = abs(second_point)
    print(ans)


