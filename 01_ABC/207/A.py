

if __name__ == '__main__':
    T = list(map(int, input().split()))
    T.sort(reverse=True)
    print(T[0]+T[1])