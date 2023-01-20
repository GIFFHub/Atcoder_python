

if __name__ == '__main__':
    A, B, W = map(int, input().split())
    W *= 1000

    min_ans = 0
    max_ans = 0

    # Aグラムのみかんを選べるだけ選ぶ場合
    # Aグラムのみかんの個数
    num_A = W // A
    # 残りのグラム数
    rest_A = W % A

    # restをAグラムのみかん全てに振り分ける
    # どのくらい振り分けるか
    if rest_A == 0:
        max_ans = num_A
    elif A + rest_A//num_A + 1 > B:
        print('UNSATISFIABLE')
        exit()
    else:
        max_ans = num_A

    num_B = W // B
    rest_B = W % B

    if rest_B == 0:
        min_ans = num_B
    elif B - rest_B // num_B - 1 < A:
        print('UNSATISFIABLE')
        exit()
    else:
        min_ans = num_B + 1

    print(min_ans, max_ans)





