

if __name__ == '__main__':
    N = int(input())
    for i in range(N+1):
        for j in range(1, 10):
            if i % (N/j) == 0:
                print(j, end='')
                break
        else:
            print('-', end='')

