

if __name__ == '__main__':
    C = input()
    s = set()
    for c in C:
        s.add(c)

    if len(s) == 1:
        print('Won')
    else:
        print('Lost')