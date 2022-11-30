import sys
sys.setrecursionlimit(1<<30)


def index(x):
    '''

    :param x: index
    :return: indexから最も近い-1となっているindex（自身を含む）
    '''

    h = x % n # 問題の指定の通りxをhに変換する

    # 既に辞書cntにindex: hが登録されている場合：すでに-1ではなくなっている
    if h in cnt:
        # cnt[h]は、else文でh+1に、もしくは本ループでさらに更新している可能性がある
        cnt[h] = index(cnt[h])
        return cnt[h]
    # 登録されていない場合：returnはそのままhでいい
    else:
        # cnt[h]はhではなく、h+1とする（hは-1ではなくなるから）
        # h+1が-1でなかったら？
        # 次hにアクセスする時、このelifにはこない
        # 上のifにいき、
        cnt[h] = (h+1) % n
        return h


if __name__ == '__main__':
    q = int(input())
    a = {} # 辞書
    cnt = {} # 辞書
    n = 1 << 20

    for _ in [None] * q:
        t, x = map(int, input().split())
        if t == 2:
            x %= n
            if x in a:
                print(a[x])
            else:
                print(-1)
        else:
            a[index(x)] = x
