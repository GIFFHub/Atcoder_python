import math

if __name__ == '__main__':
    A, B = map(int, input().split())
    K = math.lcm(A, B)
    if K > 10**18:
        print('Large')
    else:
        print(K)