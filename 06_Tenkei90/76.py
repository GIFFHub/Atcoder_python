import itertools

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    sum_A = sum(A)

    if sum_A % 10 != 0:
        print('No')
    elif sum_A//10 in A:
        print('Yes')
    else:
        A += A
        A_acc = list(itertools.accumulate(A))
        A_acc_set = set(A_acc)

        for a in A_acc:
            if sum_A//10 + a in A_acc_set:
                print('Yes')
                break
        else:
            print('No')


