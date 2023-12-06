'''
10進数(value)をn進数(base進数)に変換する
'''

def base10int(value, base):
    if (int(value // base)):
        return base10int(int(value // base), base) + str(value % base)
    return str(value % base)