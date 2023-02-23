

if __name__ == '__main__':
    S, W = map(int, input().split())
    if W >= S:
        print('unsafe')
    else:
        print('safe')