import itertools

def judge(arr, Table):
    len_arr = len(arr)
    vertex_num = len(arr[0])
    ans = 0

    for pattern in range(len_arr):
        if arr[pattern][0] == 1:
            arr_pattern = arr[pattern]
            for vertex_index in range(vertex_num):
                if vertex_index < vertex_num-1:
                    side = [arr[pattern][vertex_index], arr[pattern][vertex_index+1]]
                    side_reverse = [side[1], side[0]]
                    if side not in Table and side_reverse not in Table:
                        break
            else:
                ans += 1
    return ans


if __name__ == '__main__':
    N, M = map(int, input().split())
    Table = []
    for _ in range(M):
        Table.append(list(map(int, input().split())))
    arr = list(itertools.permutations([X+1 for X in range(N)]))
    print(judge(arr, Table))


