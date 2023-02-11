from collections import deque

if __name__ == '__main__':
    N = int(input())
    C = input()
    T = []

    R_index = deque()
    W_index = deque()
    for i, c in enumerate(C):
        if c == 'R':
            R_index.append(i)
        else:
            W_index.append(i)

    len_R = len(R_index)
    len_W = len(W_index)
    ans = 0
    if len_R == 0 or len_W == 0:
        ans = 0
    else:
        while True:
            target_W = W_index.popleft()
            target_R = R_index.pop()
            if target_W < target_R:
                ans += 1
            else:
                break
            if len(W_index) == 0 or len(R_index) == 0:
                break

    print(ans)







