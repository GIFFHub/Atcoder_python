
if __name__ == '__main__':
    N = int(input())
    i = 1
    while True:
        if int(str(i)*2) > N:
            print(i-1)
            break
        i += 1