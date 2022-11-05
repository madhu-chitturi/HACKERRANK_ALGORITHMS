                                                        Time Conversion



s=list(input())
n=len(s)
if(s[n-2]=='A'):
    if(s[0]=='1' and s[1]=='2'):
        s[0]='0'
        s[1]='0'
    s.remove('A')
    s.remove('M')
    for k in s:
        print(k,end="")
else:
    if(s[0]=='1' and s[1]=='2'):
        s.remove('P')
        s.remove('M')
        for k in s:
            print(k,end="")
    else:    
        x=s[0]+s[1]
        y=int(x)
        z=y+12
        w=list(str(z))
        s[0]=w[0]
        s[1]=w[1]
        s.remove('P')
        s.remove('M')
        for k in s:
            print(k,end="")
    
