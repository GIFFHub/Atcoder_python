

if __name__ == '__main__':
    N = int(input())
    W = list(input().split())
    S = set()
    for w in W:
        S.add(w)

    if 'and' in S:
        print('Yes')
    elif 'not' in S:
        print('Yes')
    elif 'that' in S:
        print('Yes')
    elif 'the' in S:
        print('Yes')
    elif 'you' in S:
        print('Yes')
    else:
        print('No')

