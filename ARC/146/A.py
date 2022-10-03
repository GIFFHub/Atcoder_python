import itertools

if __name__ == '__main__':

    N = int(input())
    A = list(input().split())
    A.sort(reverse=True)

    A_digits = [0]*N
    for i in range(N):
        A_digits[i] = len(A[i])

    # 最大桁
    max_digits = max(A_digits)
    # 最大桁の値の個数
    max_digits_num = A_digits.count(max_digits)

    # 最大桁の要素が3つ以上の場合
    if max_digits_num >= 3:
        print('%s%s%s' % (A[0], A[1], A[2]))

    # 最大桁の要素が2つの場合
    if max_digits_num == 2:
        tmp1 = A[0]
        tmp2 = A[1]
        next_digits = len(A[2]) # 次に大きい桁


    # 最大桁、次に大きい桁がそれぞれ１要素ずつの場合




