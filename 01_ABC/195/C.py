

if __name__ == '__main__':
    N = input()

    if len(N) % 3 == 1:
        print(len(N)//3 -1)
    else:
        print(len(N)//3)
