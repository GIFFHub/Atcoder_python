
if __name__ == '__main__':
    X = int(input())
    # a⁵-b⁵=(a-b)(a⁴+a³b+a²b²+ab³+b⁴)

    for a in range(-121, 121):
        for b in range(-121, 121):
            if a**5 - b**5 == X:
                print(a, b)
                exit()
