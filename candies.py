n=int(input())
l=list(map(int,input().split()))
total_time=0
while(1):
    l=sorted(l)
    if(len(l)>2):
        total_time=total_time+l[0]+l[1]
        dv=l[0]+l[1]
    elif(len(l)==2):
        total_time+=l[0]+l[1]
        break
    l=l[2:]
    l.append(dv)
print(total_time)
        
