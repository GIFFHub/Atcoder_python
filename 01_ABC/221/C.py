from itertools import product


if __name__ == '__main__':
    N = list(input())
    ans = 0
    for pro in product((0, 1), repeat=len(N)):
        left = []
        right = []
        for i, p in enumerate(pro):
            if p == 0:
                left.append(N[i])
            else:
                right.append(N[i])
        left.sort(reverse=True)
        right.sort(reverse=True)
        if len(left) > 0 and len(right) > 0:
            if left[0] != '0' and right[0] != '0':
                ans = max(ans, int(''.join(left)) * int(''.join(right)))
    print(ans)






