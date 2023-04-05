
if __name__ == '__main__':
    A, B = map(int, input().split())
    if 6 <= A <= 12:
        print(B//2)
    elif A <= 5:
        print(0)
    else:
        print(B)
