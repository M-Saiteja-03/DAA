n=int(input("no of subjects: "))
sub=[]
for i in range(n):
    print("Enter subject_code and subject_name for {}".format(i+1))
    l=list(map(str,input().split()))
    sub.append(l)
print(sub)      

x=[0 for x in range(n)]
G=[[0 for i in range(n)]for i in range(n)]
#print(G)
for i in range(n):
    print("Enter clashes for subject {}".format(i+1))
    l=list(map(int,input().split()))

    for j in l:
        G[i][j-1]=1
print(G)

def TimeScheduling(k,i):
    while(i==True):
        NextValue(k)
        if(x[k]==0):
            return
        if(k==n-1):
            # print(*subject_details)
            print("Time line schedule seqquence is : ",*x)
            solution=True
            exit(0)
            i=False
        else:
            i=TimeScheduling(k+1,i)
            
def NextValue(k):
    while(True):
       # print("@@",*x)
        x[k]=(x[k]+1)%(m+1)
        #print("))",k)
        if (x[k]==0):
            return 
        for j in range(n):
            #print("**",j)
            if (G[k][j]!=0 and x[k]==x[j]):
                break
        if(j==n-1):
            return
for m in range(1,n+1):
    TimeScheduling(0,True)
    x=[0 for x in range(n)]
    
#TimeScheduling(0,True)

# n=int(input("No of vertices: "))
# x=[0]*(n)
# res=[]
# flag=0
# m=int(input("Max colors to be used : "))
# g=[[0,1,0,1,0],[1,0,1,0,0],[0,1,0,1,1],[1,0,1,0,1],[0,0,1,0,0]]
# def mColoring(k,i):
#     while i==True:
#         NextValue(k)
#         if x[k]==0:
#             return
#         if k==n-1:
#             print("The required color code for each node is: ")
#             print(x)
#             res.append(x)
#             flag=1
#             i=False
#             return i
#         else:
#             i=mColoring(k+1,i)
# def NextValue(k):
#     while True:
#         x[k]=(x[k]+1)%(m+1)
#         if x[k]==0:
#             return False
#         for j in range(n):
#             if g[k][j]==1 and x[k]==x[j]:
#                 break
#             if j==n-1:
#                 return
# mColoring(0,True)
# if len(res)==0:
#     print("Not enough colors")