import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
4
4 7 3 7
1
313
10
999999997 999999999 4 3 2 4 999999990 8 999999991 999999993
"""

def solve(test):
  N=int(input())
  A=list(map(int, input().split()))
  n,m=sum(A)//N,sum(A)%N
  if m==0:
    ans=sum([abs(A[i]-n) for i in range(N)])//2
  else:
    ans=0
    tmp=0
    for i in range(N):
      if A[i]<=n:
        ans+=n-A[i]
      else:
        ans+=A[i]-n-1
        tmp+=1
    ans+=abs(m-tmp)
    ans//=2
  if test==0:
    print(ans)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)