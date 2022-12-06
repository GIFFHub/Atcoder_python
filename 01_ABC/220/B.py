def base_10(num_n, n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10


if __name__ == '__main__':
    K = int(input())
    A, B = map(int, input().split())

    A = base_10(A, K)
    B = base_10(B, K)

    print(A*B)

