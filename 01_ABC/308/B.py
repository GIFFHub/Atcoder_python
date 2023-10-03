

if __name__ == '__main__':
    N, M = map(int, input().split())
    C = list(input().split())
    D = list(input().split())
    P = list(map(int, input().split()))

    price = dict()
    for i in range(M):
        price[D[i]] = P[i+1]

    sum_price = 0
    for c in C:
        if c in price:
            sum_price += price[c]
        else:
            sum_price += P[0]
    print(sum_price)