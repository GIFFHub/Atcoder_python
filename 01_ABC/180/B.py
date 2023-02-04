import math

if __name__ == '__main__':
    N = int(input())
    X = list(map(int, input().split()))
    ans_m = 0
    ans_u = 0
    ans_c = 0
    for x in X:
        abs_x = abs(x)
        ans_m += abs_x
        ans_u += abs_x**2
        ans_c = max(ans_c, abs_x)
    ans_u = math.sqrt(ans_u)

    print(ans_m)
    print(ans_u)
    print(ans_c)




