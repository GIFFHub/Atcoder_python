
import math
import bisect

if __name__ == '__main__':
    D = int(input())

    ans = 1414213123123412
    T = []
    for x in range(0, 1500000):
        if x**2 > D:
            break
        T.append(x**2)

    len_T = len(T)

    for i in range(len_T):
        x2 = T[i]
        y2_index = bisect.bisect(T, D-x2)
        if y2_index - 3 >= 0:
            ans = min(ans, abs(x2 + T[y2_index-3] - D))
        if y2_index - 2 >= 0:
            ans = min(ans, abs(x2 + T[y2_index-2] - D))
        if y2_index - 1 >= 0:
            ans = min(ans, abs(x2 + T[y2_index-1] - D))
        if y2_index < len_T:
            ans = min(ans, abs(x2 + T[y2_index] - D))
        if y2_index + 1 < len_T:
            ans = min(ans, abs(x2 + T[y2_index+1] - D))
    if ans < 0:
        ans = 0
    print(ans)


