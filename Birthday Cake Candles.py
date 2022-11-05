
link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

n=int(input())
arr=list(map(int,input().strip().split()))
x=max(arr)
y=arr.count(x)
print(y)
