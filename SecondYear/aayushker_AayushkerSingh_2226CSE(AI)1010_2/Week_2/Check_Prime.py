from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
c=0

if(n == 1):
    print("NO")

else:
    for i in range(2, int(sqrt(n)+1), 1):
        if(n%i == 0):
            c += 1
            if(c>0):
                break

    if(c == 0):
        print("YES")

    else:
        print("NO")  
