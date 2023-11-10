from collections import defaultdict

if __name__ == '__main__':
    N = int(input()) # スライムの種類数
    d = dict()

    for _ in range(N):
        S, C = map(int, input().split())
        cnt = 0
        tmp_S = S
        while True:
            if tmp_S % 2 == 1:
                break
            else:
                tmp_S //= 2
                cnt += 1
        if tmp_S in d:
            d[tmp_S].append(S*C)
        else:
            d[tmp_S] = [S*C]

    for key in d.keys():
        tmp_value = sum(d[key])
        tmp_value //= key
        d[key] = tmp_value

    ans = 0
    for value in d.values():
        bin_value = bin(value)
        for b in bin_value:
            if b == '1':
                ans += 1
    print(ans)








