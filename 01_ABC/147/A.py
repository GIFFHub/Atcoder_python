

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if sum(A) >= 22:
        print('bust')
    else:
        print('win')