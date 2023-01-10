

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    M_A = max(A)
    m_B = min(B)

    print(max(0, m_B-M_A+1))

