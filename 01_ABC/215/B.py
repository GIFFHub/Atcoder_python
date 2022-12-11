import math

if __name__ == '__main__':
    N = int(input())
    cnt = 1
    while True:
        if math.pow(2, cnt) > N:
            print(cnt-1)
            break
        cnt += 1

