

if __name__ == '__main__':
    T = []
    for i in range(5):
        T.append(int(input()))
    k = int(input())

    T.sort()
    if T[-1] - T[0] > k:
        print(':(')
    else:
        print('Yay!')