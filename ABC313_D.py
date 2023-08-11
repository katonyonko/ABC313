N,K=map(int,input().split())
if N>=2*K-2:
  li=[]
  for i in range(N-K+1):
    print('?', i+1, *[N-K+2+j for j in range(K-1)])
    li.append(int(input()))
  tmp=0
  for i in range(K-1):
    print('?', N-K+2+i, *[j+1 for j in range(K-1)])
    li.append(int(input()))
    tmp^=li[-1]
  ans=[]
  for i in range(N-K+1):
    ans.append(tmp^li[i])
  tmp=0
  for i in range(K-1):
    tmp^=li[i]
  for i in range(K-1):
    ans.append(tmp^li[N-K+1+i])
  print('!', *ans)
else:
  li=[]
  tmp=0
  for i in range((K-1)//2):
    print('?', 2*i+1, *([j+1 for j in range(2*i)]+[j+2*i+3 for j in range(K-1-2*i)]))
    li.append(int(input())^tmp)
    print('?', 2*i+2, *([j+1 for j in range(2*i)]+[j+2*i+3 for j in range(K-1-2*i)]))
    li.append(int(input())^tmp)
    tmp^=li[-1]
    tmp^=li[-2]
  ans=[-1]*N
  for i in range(N-K+1):
    print('?', K+i, *[j+1 for j in range(K-1)])
    li.append(int(input()))
    ans[K-1+i]=tmp^li[-1]
  tmp=ans[K-1]^ans[K]
  for i in reversed(range((K-1)//2)):
    ans[2*i]=li[2*i]^tmp
    ans[2*i+1]=li[2*i+1]^tmp
    tmp^=ans[2*i]
    tmp^=ans[2*i+1]
  print('!', *ans)