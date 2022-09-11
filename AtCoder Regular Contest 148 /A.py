import numpy as np


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def remove_specified_values(arr, value):
    while value in arr:
        arr.remove(value)


if __name__ == '__main__':
    N = int(input())
    A = sorted(list(map(int, input().split())))
    A = np.array(A)
    A = np.diff(A)

    remove_specified_values(list(A), 0)

    if len(A) < 2:
        print(1)
    elif A[0] == 1:
        if max(A) == 1:
            print(1)
        else:
            print(2)
    else:
        # 全部同じ数の倍数の場合：1
        # それ以外：2
        A0_div = make_divisors(A[0])
        A0_div.pop(0)

        for x in A0_div: # 約数
            for a in A:  # Aの要素
                if a%x == 0: # 倍数の場合
                    pass
                else:
                    break
            else: # breakしなかった場合（全て倍数だった場合）
                print(1)
                exit()
        print(2)




