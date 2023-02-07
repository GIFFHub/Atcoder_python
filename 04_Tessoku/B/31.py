

if __name__ == '__main__':
    N = int(input())
    num_3 = N // 3
    num_5 = N // 5
    num_7 = N // 7
    num_3_5 = N // 15
    num_3_7 = N // 21
    num_5_7 = N // 35
    num_3_5_7 = N // 105

    ans = (num_3+num_5+num_7) - (num_3_5+num_3_7+num_5_7) + num_3_5_7

    print(ans)
