

if __name__ == '__main__':
    S = input()
    ans = []
    for s in S:
        if s == '0':
            ans.append('1')
        else:
            ans.append('0')
    print(''.join(ans))


