from collections import defaultdict
import math

if __name__ == '__main__':
    K = int(input())
    S = input()
    T = input()
    card_all = defaultdict(int)
    card_s = defaultdict(int)
    card_t = defaultdict(int)
    ans = 0

    for i in range(1, 10):
        card_all[i] = K

    for s in S[:4]:
        card = int(s)
        card_s[card] += 1
        card_all[card] -= 1

    for t in T[:4]:
        card = int(t)
        card_t[card] += 1
        card_all[card] -= 1

    # 高橋くんの残りカード候補
    for card_s_last in range(1, 10):
        if card_all[card_s_last] == 0:
            continue

        # 高橋くんの残りカードが[card_s_last]である確率
        p_s = card_all[card_s_last] / (9 * K - 8)
        #print('p_s:', p_s)
        card_s[card_s_last] += 1
        card_all[card_s_last] -= 1

        # 高橋くんの残りカードが[card_s_last]の時の高橋くんの得点
        point_s = 0
        for i in range(1, 10):
            point_s += i * math.pow(10, card_s[i])

        # 青木くんの残りカード候補
        for card_t_last in range(10):
            if card_all[card_t_last] == 0:
                continue

            # 青木くんの残りカードが[card_t_last]である確率
            p_t = card_all[card_t_last] / (9 * K - 9)
            #print('p_t:', p_t)
            card_t[card_t_last] += 1
            card_all[card_t_last] -= 1

            # 青木くんの残りカードが[card_t_last]の時の青木くんの得点
            point_t = 0
            for i in range(1, 10):
                point_t += i * math.pow(10, card_t[i])

            if point_s > point_t:
                ans += p_s*p_t

            card_all[card_t_last] += 1
            card_t[card_t_last] -= 1
        card_all[card_s_last] += 1
        card_s[card_s_last] -= 1

    print(ans)

















