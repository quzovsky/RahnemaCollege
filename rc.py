n=input()
l=[]
while True:
    t=list(map(str,input().split(' ')))
    if t[0]=='':
        break
    l.append(t)
l1=[list(x) for x in zip(*l)]
sum=[0]*len(l)
for i in range(4):
    for j in range(len(l)):
        if l1[i][j].startswith(n):
            if l1[i].count(l1[i][j])==1:
                sum[j]+=10
            if l1[i].count(l1[i][j])>=2:
                sum[j]+=5
        
for i in range(len(sum)):
    print(f"Player number {i+1} scored {sum[i]} points.")