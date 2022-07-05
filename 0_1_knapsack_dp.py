# 0/1 Knapsack using DP🤐 
def dp_knapsack(l,m):
    B=[[0 for i in range(m+1)] for j in range(len(l)+1)]
    for i in range(len(l)):
        for w in range(1,m+1):
            if w<0:
                B[i][w]=0
            else:
                if l[i][0]>w:
                    B[i][w]=B[i-1][w]
                elif l[i][0]<=w:
                    B[i][w]=max(B[i-1][w],B[i-1][w-l[i][0]]+l[i][1])
    print("The table we get from tabulation method is:")
    for i in range(-1,n):
        print(B[i])
    x=[0 for i in range(len(l))]
    i=len(l)-1
    k=m
    max_profit=B[i][k]
    while (i>=0 and k>0):
        if B[i][k]!=B[i-1][k]:
            x[i]=1
            k-=l[i][0]
        #print(i,B[i][k],i-1,B[i-1][k])
        i=i-1
    print("The max profit is:",max_profit)
    print("The solution vector is:",x)
    
l=[]
m=int(input("Enter the max time capacity: "))
n=int(input("Enter the number of questions: "))
print("Enter the time and points of each question: ")  
for i in range(n):
    a,b=[int(x) for x in input().split()]
    l.append([a,b])
#print(l)
dp_knapsack(l,m)




# p=[eval(x) for x in input().split()]
# wt=[eval(x) for x in input().split()]
# m=int(input("Enter max capacity:"))
# n=len(p)
# k=[[0 for i in range(m+1)]for j in range(n+1)]
# # print(k)
# sol=[0]*n
# for i in range(n+1):
#     for w in range(m+1):
#         if(i==0 or w==0):
#             k[i][w]=0
#         elif(wt[i-1]<=w):
#             k[i][w]=max(p[i-1]+k[i-1][w-wt[i-1]],k[i-1][w])
#         else:
#             k[i][w]=k[i-1][w]
#     # print(k)
# print(k[n][w])
# i,j=n,m
# while(i>0 and j>0):
#     if(k[i][j]!=k[i-1][j]):
#         sol[i-1]=1
#         j=j-wt[i-1]
#         i=i-1
#     else:
#         i=i-1
# print(sol)