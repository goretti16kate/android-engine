import sys
import math
#from itertools import combinations
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
strengths=[]
#def tool(strengths, r):
  #  return list(combinations(strengths, r))
for i in range(n):
    pi = int(input())
    #make a list thingy
    strengths.append(pi)
strengths=sorted(strengths)

diff = 10**20
for i in range(n-1):
    if strengths[i +1] - strengths[i]< diff:
        diff = strengths[i+1] - strengths [i]

print (str(diff))