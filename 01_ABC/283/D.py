from collections import deque

if __name__ == '__main__':
    S = input()
    s = set()
    box = deque()
    tmp = deque()
    flg = 0
    for i in range(len(S)):
        if S[i] == '(':
            box.append(tmp)
            tmp = []
            flg = 1
        elif S[i] == ')':
            if flg == 1:
                flg = 2
                continue
            elif flg == 2:
                balls = box.pop()
            else:
                balls = tmp

            for ball in balls:
                s.remove(ball)
            tmp = []
            flg = 2

        else:
            if S[i] in s:
                print('No')
                break
            else:
                s.add(S[i])
                tmp.append(S[i])
            flg = 3
    else:
        print('Yes')



