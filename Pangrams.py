s1=input()
s2=s1.lower()
s=list(s2)
a=list(set(s))
x=' '
if x in a:
    a.remove(x)
if(len(a)==26):
    print("pangram")
else:
    print("not pangram")
