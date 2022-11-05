                                                                  Plus Minus

n=int(input())
arr=list(map(int,input().strip().split()))
c1=0
c2=0
c3=0
for i in range(n):
    if(arr[i]>0):
        c1+=1
    elif(arr[i]<0):
        c2+=1
    else:
        c3+=1
print(c1/n)
print(c2/n)
print(c3/n)
