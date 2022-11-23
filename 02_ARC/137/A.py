import math
L,R=map(int,input().split())
ans=R-L
check=False
while ans>0:
  for i in range(L,L+1+(R-L)-ans):
    if math.gcd(i,ans+i)==1:
      check=True
      break
  if check:
    break
  ans-=1
print(ans)