
#https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""#


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


if __name__ == '__main__':
    N = int(input())

    F = factorization(N)

    soinsu = 0
    for f in F:
        soinsu += f[1]
    if soinsu == 1:
        print(0)
    else:
        ans = 2
        cnt = 1
        while True:
            if soinsu <= ans**cnt:
                print(cnt)
                break
            cnt += 1