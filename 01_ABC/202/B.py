from collections import deque

if __name__ == '__main__':
    S = input()
    ans = deque()
    for i in range(len(S)):
        tmp = S[-i-1]
        if tmp == '6':
            ans.append('9')
        elif tmp == '9':
            ans.append('6')
        else:
            ans.append(tmp)

    print("".join(ans))