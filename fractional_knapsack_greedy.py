def merge(jo,low,mid,high):
    i,j=low,mid+1
    temp=[]
    while(i<=mid and j<=high):
        if(jo[i][3]>jo[j][3]):
            temp.append(jo[i])
            i+=1
        else:
            temp.append(jo[j])
            j+=1
    while(i<=mid):
        temp.append(jo[i])
        i+=1
    while(j<=high):
        temp.append(jo[j])
        j+=1
    for i in range(len(temp)):
        jo[low+i]=temp[i]
    return jo
def ms(jo,low,high):
    if(low<high):
        mid=(low+high)//2
        ms(jo,low,mid)
        ms(jo,mid+1,high)
        merge(jo,low,mid,high)
    return jo
w=[eval(x) for x in input("Enter weights:").split()]
p=[eval(x) for x in input("Enter profits:").split()]
m=int(input("max capacity:"))
n=len(w)
job=[]
tw=0
tp=0
sol=[0]*n
for i in range(n):
    job.append((i,p[i],w[i],p[i]/w[i]))
l=ms(job,0,n-1)
print(l)
for j in range(n):
    if l[j][2]<=m-tw:
        tw=tw+l[j][2]
        tp=tp+l[j][1]
        sol[l[j][0]]=1
    else:
        if(m-tw!=0):
            tp=tp+l[j][1]*((m-tw)/l[j][2])
            sol[l[j][0]]=(m-tw)/l[j][2]
            tw=m
print(sol,tp)
