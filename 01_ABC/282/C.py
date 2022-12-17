from collections import deque


if __name__ == '__main__':
    N = int(input())
    S = input()
    ans = deque()
    target = "\""
    flg = 0
    for s in S:
        if s == target and flg == 0:
            ans.append(target)
            flg = 1
        elif s == target and flg == 1:
            ans.append(target)
            flg = 0
        elif s == ',' and flg == 0:
            ans.append(".")
        else:
            ans.append(s)

    print("".join(ans))

        
    

    


