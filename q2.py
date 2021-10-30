def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n,m = map(int,input().split())
n=min(n,m)
m=max(n,m)
if n==1:
    n+=1

for i in range(n,m+1):
    if prime(i):
        print(i,end="\t")