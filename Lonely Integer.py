#!/bin/python3

import math
import os
import random
import re
import sys
def lonelyinteger(a):
    # Write your code here
    c=list(set(a))
    for i in range(len(c)):
        b=a.count(c[i])
        if(b==1):
            return c[i]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
