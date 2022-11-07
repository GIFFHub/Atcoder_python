

if __name__ == '__main__':
    # input
    A, B = map(int, input().split())
    str_A = str(A)
    str_B = str(B)

    # check all digit
    min_digit = min(len(str_A), len(str_B))
    for i in range(1, min_digit+1):
        if int(str_A[-i]) + int(str_B[-i]) >= 10:
            print('Hard')
            break
    else:
        print('Easy')


