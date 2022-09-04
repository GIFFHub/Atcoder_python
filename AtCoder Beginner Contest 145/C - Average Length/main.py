import itertools
import math


def cul_average_distance(arr, town_pos):
    len_arr = len(arr)
    len_town_pos = len(town_pos)
    sum_distance = 0
    for pattern in range(len_arr):
        for Town in range(len_town_pos):
            if Town < len_town_pos - 1:
                current_town_pos = town_pos[arr[pattern][Town]]
                next_town_pos = town_pos[arr[pattern][Town + 1]]
                sum_distance += cul_distance(current_town_pos, next_town_pos)

    return sum_distance / len_arr


def cul_distance(pos_1, pos_2):
    distance = math.sqrt((pos_1[0] - pos_2[0]) ** 2 + (pos_1[1] - pos_2[1]) ** 2)
    return distance


if __name__ == '__main__':
    N = int(input())
    Town_pos = []
    for _ in range(N):
        Town_pos.append(list(map(int, input().split())))
    arr = list(itertools.permutations([x for x in range(N)]))
    print(cul_average_distance(arr, Town_pos))
