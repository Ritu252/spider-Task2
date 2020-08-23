n = int(input())
a = []
for i in range(n):
    a.append(i)
q = int(input())
if 1<=n<=10**5 and 1<=q<=10**5:
    for i in range(q):
        k = list(map(int,input().split()))
        if k[1]>=n:
            for i in range(k[0],n):
                a[i]+=k[2]
        else:
            for i in range(k[0],k[1]+1):
                a[i]+=k[2]
                
                
print(max(a))
