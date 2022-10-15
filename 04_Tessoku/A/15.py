input()
A = list(map(int, input().split()))
A_tmp = sorted(list(set(A)))
A_dict = {x: y for x, y in zip(A_tmp, range(1, len(A_tmp)+1))}
B = [A_dict[a] for a in A]
print(*B)