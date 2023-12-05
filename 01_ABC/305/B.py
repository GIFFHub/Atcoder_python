

if __name__ == '__main__':
    p, q = input().split()
    d = dict()
    d['A'] = 0
    d['B'] = 3
    d['C'] = 4
    d['D'] = 8
    d['E'] = 9
    d['F'] = 14
    d['G'] = 23

    print(abs(d[p]-d[q]))
