import math

if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        x = int(input())
        rx = int(math.sqrt(x))+1

        for i in range(2, rx):
            if x % i == 0:
                print('No')
                break
        else:
            print('Yes')

