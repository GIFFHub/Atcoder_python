
N = int(input())

S = []
for i in range(1, N+1):
    if i == 1:
        S.append(str(i))
    else:
        S.append(S[i-2]+' '+str(i)+' '+S[i-2])

print(S[-1])


