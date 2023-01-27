ans=float('inf')
def cost(arr,A):
    s=0
    for i in range(len(arr)):
        s+=abs(arr[i]-A[i])
    return s
def ismagic(arr):
    r1=arr[0]+arr[1]+arr[2]
    r2=arr[3]+arr[4]+arr[5]
    r3=arr[6]+arr[7]+arr[8]
    c1=arr[0]+arr[3]+arr[6]
    c2=arr[1]+arr[4]+arr[7]
    c3=arr[2]+arr[5]+arr[8]
    d1=arr[0]+arr[4]+arr[8]
    d2=arr[2]+arr[4]+arr[6]
    if(r1==r2 and r2==r3) and (c1==c2 and c2==c3) and (d1==d2):
        return True
    else:
        return False
def generate(arr,c,idx,A):
    global ans
    if(idx==9):
        if(ismagic(arr)):
            cc=cost(arr,A)
            ans=min(ans,cc)
    for i in range(1,10):
        if(c[i]=='F'):
            arr[idx]=i
            c[i]='T'
            generate(arr,c,idx+1,A)
            c[i]='F'
            
A=[]
for i in range(3):
    a=list(map(int,input().strip().split()))
    A+=a
arr=[0,0,0,0,0,0,0,0,0]
c=['F','F','F','F','F','F','F','F','F','F']
ans=float('inf')
generate(arr,c,0,A)
print(ans)
