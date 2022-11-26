

if __name__ == '__main__':
    S = input()
    ans = 0
    ans += S.count('v')
    ans += 2*(S.count('w'))

    print(ans)