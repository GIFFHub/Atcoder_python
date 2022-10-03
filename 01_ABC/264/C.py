from itertools import product
from sys import stdin
import numpy as np

def judge(line_index, column_index,  queue1, queue2):
    for i in range(len(line_index)):
        for j in range(len(column_index)):
            if queue1[line_index[i]][column_index[j]] != queue2[i][j]:
                return False
    return True


def main():
    H1, W1 = map(int, input().split())
    A = np.array([list(map(int, stdin.readline().split())) for _ in range(H1)])
    H2, W2 = map(int, input().split())
    B = np.array([list(map(int, stdin.readline().split())) for _ in range(H2)])

    for bits in product((0, 1), repeat=H1+W1):
        line_bits = bits[:H1]
        column_bits = bits[H1:]

        if line_bits.count(1) == H2 and column_bits.count(1) == W2:
            line_index = [j for j, x in enumerate(line_bits) if x == 1]
            column_index = [j for j, x in enumerate(column_bits) if x == 1]
            if judge(line_index, column_index, A, B):
                print('Yes')
                break
    else:
        print('No')

main()
