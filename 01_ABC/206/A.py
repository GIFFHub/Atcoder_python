import math

if __name__ == '__main__':
    N = int(input())
    x = round(1.08 * N)

    if x < 206:
        print('Yay!')
    elif x == 206:
        print('so-so')
    else:
        print(':(')
