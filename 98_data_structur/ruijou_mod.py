

def power(a, b, m):
    '''
    (a**b) % m を高速で返す
    '''
    p = a
    answer = 1
    for i in range(30):
        # wari : pがaの何乗になっているか
        wari = 2 ** i
        # 2進数表記でbitが立っているかどうか判定
        # (10進数を2進数に変換する処理と同じ)
        # bitが立っている場合、2のbit桁乗は乗算される
        if (b//wari) % 2 == 1: # bitが立っている場合、構成要素になる
            answer = (answer*p) % m
        p = (p*p) % m
    return answer
