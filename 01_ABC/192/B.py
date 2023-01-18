

if __name__ == '__main__':
    S = input()
    flg = 1
    ans = 'Yes'
    for s in S:
        if flg:
            if s.isupper():
                ans ='No'
                break
            else:
                flg = 1-flg
        else:
            if s.islower():
                ans = 'No'
                break
            else:
                flg = 1-flg
    print(ans)
