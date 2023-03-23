

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(max(A+B, A-B, A*B))