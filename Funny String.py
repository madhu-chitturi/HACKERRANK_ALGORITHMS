                                                              Funny String


t=int(input())
for i in range(t):
    s=list(input())
    a=s[::-1]
    b=[]
    c=[]
    d=[]
    g=[]
    for j in range(len(s)):
        e=ord(a[j])
        f=ord(s[j])
        b.append(e)
        c.append(f)
    for k in range(1,len(c)):
        r=abs(c[k]-c[k-1])
        r1=abs(b[k]-b[k-1])
        d.append(r)
        g.append(r1)
    if(d==g):
        print("Funny")
    else:
        print("Not Funny")
