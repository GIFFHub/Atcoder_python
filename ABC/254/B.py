
if __name__ == '__main__':
    N = int(input())
    tmp = 0
    prev_arr = [0]
    current_arr = []

    for i in range(N):
        prev_arr = current_arr
        current_arr = []
        for j in range(i+1):
            if j == 0:
                tmp = 1
                current_arr.append(tmp)
                print('%d' % tmp, end='')
            elif j == i:
                tmp = 1
                current_arr.append(tmp)
                print(' %d' % tmp, end='')
            else:
                if len(prev_arr) > 1:
                    tmp = prev_arr[j-1]+prev_arr[j]
                else:
                    tmp = prev_arr[j-1]
                current_arr.append(tmp)
                print(' %d' % tmp, end='')
        print()


