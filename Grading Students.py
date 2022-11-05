                                              Grading Students
  
  
n = int(input().strip())
for i in range(n):
    x = int(input())
    if x >= 38:
        if x % 5 > 2:
            while x % 5 != 0:
                x += 1
    print(x)
