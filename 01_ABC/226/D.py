
import math


def cal_vector(pos_i, pos_j):
    dx = pos_i[0]-pos_j[0]
    dy = pos_i[1]-pos_j[1]

    while True:
        tmp = math.gcd(dx, dy)
        if tmp != 1:
            dx /= tmp
            dy /= tmp
        else:
            break
    return (dx, dy)



if __name__ == '__main__':
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    '''
    考察
    ・全町から他の町までのベクトルを全列挙して
    ・方向が同じ重複を削除すれば答えがでるが、TLE？
    ・N＝500の場合、499通りのベクトルが500個
    '''
