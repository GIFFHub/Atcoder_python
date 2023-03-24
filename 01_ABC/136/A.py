

if __name__ == '__main__':
    A, B, C = map(int, input().split())
    rest = A - B
    print(max(0, C - rest))