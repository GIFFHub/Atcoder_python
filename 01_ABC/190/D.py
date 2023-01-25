
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

    T = factorization(2*N)

    ans = 1
    for i in range(1, len(T)):
        ans *= (T[i][1]+1)

    ans *= 2
    print(ans)

