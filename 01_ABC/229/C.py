

if __name__ == '__main__':
    N, W = map(int, input().split())
    A = []
    B = []
    Cheeses = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        Cheeses.append([a, b])

    # simply, we can use the delicious cheese as much as possible

    # sort by deliciousness of cheese
    Cheeses.sort(reverse=True, key=lambda x: x[0])

    # use cheese until the limit(W)
    deliciousness = 0
    cnt = 0
    weight = 0
    for i in range(N):
        # judge whether we can all cheese
        tmp_deliciousness = Cheeses[i][0]
        tmp_amount = Cheeses[i][1]

        remain_amount = min(W-weight, tmp_amount)
        if remain_amount == 0:
            break

        deliciousness += tmp_deliciousness * remain_amount
        weight += remain_amount

    print(deliciousness)

