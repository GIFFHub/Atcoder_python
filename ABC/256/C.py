if __name__ == '__main__':
    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    ans = 0
    for i in range(1, w1):  # 左上
        for j in range(1, w1 - i):  # 右上
            for k in range(1, h3 - j):  # 右下
                for l in range(1, w3 - k):  # 左下
                    up = w1 - i - j
                    right = h3 - j - k
                    down = w3 - k - l
                    left = h1 - i - l
                    if min(up, right, down, left) > 0:
                        center1 = w2 - left - right
                        center2 = h2 - up - down
                        if center1 == center2 and center1 > 0:
                            ans += 1

    print(ans)
