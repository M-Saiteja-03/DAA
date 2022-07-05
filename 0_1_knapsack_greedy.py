class Question:
    def __init__(self,points,time,x):
        self.points=points
        self.time=time
        self.x=x

def merge(l,low,high,mid):
    temp=[]
    i=low
    j=mid+1
    while(i<=mid and j<=high):
        if ((l[i].points/l[i].time)>(l[j].points/l[j].time)):
            temp.append(l[i])
            i+=1
        else:
            temp.append(l[j])
            j+=1
    while(i<=mid):
        temp.append(l[i])
        i+=1
    while(j<=high):
        temp.append(l[j])
        j+=1
    for i in range(len(temp)):
        l[low+i]=temp[i]
   
def merge_sort(l,low,high):
    mid=(low+high)//2
    if(low<high):
        merge_sort(l,low,mid)
        merge_sort(l,mid+1,high)
        merge(l,low,high,mid)
    return l

def knapsack(l,m):
    u=m
    total=0
    vector=[0]*(len(l))
    for i in range(len(l)):
        if u-l[i].time>=0 :
            vector[i]=1
            l[i].x=1
            u-=l[i].time             
        else:
            l[i].x=0
    return vector
l=[]
n=int(input("Input the size of array: "))
for i in range(n):
    points=int(input("points: "))
    time=int(input("time: "))
    l.append(Question(points,time,0))
s=[]
for i in range(len(l)):
    s.append(l[i])
m=int(input("Enter the max time capacity: "))
merge_sort(l,0,len(l)-1)
result=knapsack(l,m)
max_score=0
for i in range(len(l)):
    max_score+=l[i].points*result[i]
arr=[]
for i in range(len(s)):
    arr.append(s[i].x)
print("The result vector x is:",arr)
print("The maximum score is obtained: ",max_score)
