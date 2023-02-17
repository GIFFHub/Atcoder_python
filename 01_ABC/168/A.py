

if __name__ == '__main__':
    N = input()
    hon = {2, 4, 5, 7, 9}
    pon = {0, 1, 6, 8}
    bon = {3}
    last = int(N[-1])

    if last in hon:
        print('hon')
    elif last in pon:
        print('pon')
    else:
        print('bon')
