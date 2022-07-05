class Job:
    def __init__(self,profit,deadline,q_no):
        self.profit=profit
        self.deadline=deadline
        self.q=q_no

def merge(l,low,high,mid):
    i=low
    j=mid+1
    temp=[]
    while(i<=mid and j<=high):
        if (l[i].profit>l[j].profit):
            temp.append(l[i])
            i+=1
        else:
            temp.append(l[j])
            j+=1
    while (i<=mid):
        temp.append(l[i])
        i+=1
    while (j<=high):
        temp.append(l[j])
        j+=1
    for i in range(len(temp)):
        l[low+i]=temp[i]
    return l

def merge_sort(l,low,high):
    mid=(low+high)//2
    if (low<high):
        merge_sort(l,low,mid)
        merge_sort(l,mid+1,high)
        merge(l,low,high,mid)
    return l

def job_scheduling(l):
    l=merge_sort(l,0,len(l)-1)
    max_deadline=0
    for i in range(len(l)):
        if l[i].deadline>max_deadline:
            max_deadline=l[i].deadline
    x=[None]*(max_deadline)

    for j in range(len(l)):
        ind=l[j].deadline-1
        if x[ind]==None:
            x[ind]=l[j]
        else:
            count=ind
            for k in range(count,-1,-1):
                '''ind-=1
                if ( ind>=0 and x[ind]==None):
                    x[ind]=l[i]
                    break'''
                if x[k]==None:
                    x[k]=l[j]
                    break

    return x

n=int(input("Enter the no of Jobs: "))
qs=[]
print("Enter Pi: profit and Di: deadline for each Ji")
for i in range(n):
    profit,deadline=[int(x) for x in input().split()]
    qs.append(Job(profit,deadline,i+1))
result=job_scheduling(qs)
total=0
l=[]
for i in range(len(result)):
    if result[i] is not None:
        total+=result[i].profit
        l.append(result[i].q)
print("The Jobs subset is:",l)
print("The max profit within deadline is:",total)


# process=[eval(x) for x in input("Enter the id:").split()]
# pro=[eval(x) for x in input("Enter the profits:").split()]
# dl=[eval(x) for x in input("Enter the deadlines:").split()]
# n=len(pro)
# job=[]
# tp=0
# for i in range(n):
#     job.append([process[i],pro[i],dl[i]])
# job.sort(key=lambda x:x[1],reverse=True)
# print(job)
# dlsp=[i[1] for i in job]
# m=max(dlsp)
# l=[0]*m
# for i in job:
#     ind=i[2]
#     while(ind!=0):
#         if(l[ind-1]==0):
#             l[ind-1]=i[0]
#             tp=tp+i[1]
#             break
#         else:
#             ind-=1
# print(l)
# print(tp)