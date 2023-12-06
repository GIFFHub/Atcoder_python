from itertools import product

if __name__ == '__main__':
    N = int(input())
    score = 0
    for pro in product((0, 1), repeat=N):
        score = 0
        for p in pro:
            if p == 0:
                score += 1
            else:
                score -= 1
            if score < 0:
                break
        else:
            if score == 0:
                ans = ''
                for p in pro:
                    if p == 0:
                        ans += '('
                    else:
                        ans += ')'
                print(ans)


