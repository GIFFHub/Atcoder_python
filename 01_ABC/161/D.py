

if __name__ == '__main__':
    K = int(input())

    ans = [0]

    for _ in range(K):
        keta = 0
        if set(ans) == {9}:
            ans.append(1)
            for i in range(len(ans)-1):
                ans[i] = 0
        else:
            if ans[0] != 9:
                ans[0] += 1
            else:
                # ans[0]を11にすれば勝手に修正される
                ans[0] += 2
            while len(ans) > keta + 1:
                if abs(ans[keta+1] - ans[keta]) > 1:
                    ans[keta+1] = (ans[keta+1]+1) % 10
                    for k in range(keta, -1, -1):
                        ans[k] = max(0, ans[k+1]-1)
                    keta += 1
                else:
                    break
    ans.reverse()
    answer = ''
    for a in ans:
        answer += str(a)
    print(answer)








