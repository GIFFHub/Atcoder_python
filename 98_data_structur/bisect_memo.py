
import bisect
if __name__ == '__main__':

    T = [1, 1, 3]

    '''
    bisect.bisect
    配列を挿入した場合のインデックスを返す。
    同じ値がある場合は一番右に挿入するようにする。
        bisect_leftの場合のみ、一番左に挿入するようにする。
    '''
    index_1 = bisect.bisect(T, 1) # 2
    index_2 = bisect.bisect(T, 2) # 2
    index_3 = bisect.bisect(T, 3) # 3

    index_left_1 = bisect.bisect_left(T, 1) # 0
    index_left_2 = bisect.bisect_left(T, 2) # 2
    index_left_3 = bisect.bisect_left(T, 3) # 2

    index_right_1 = bisect.bisect_right(T, 1) # 2
    index_right_2 = bisect.bisect_right(T, 2) # 2
    index_right_3 = bisect.bisect_right(T, 3) # 3

    print(1)
