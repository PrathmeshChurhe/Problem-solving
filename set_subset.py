# determine whether the set A is subset of set B using input() method

# optimal method for problem

for i in range(int(input())):
  a=int(input()); A=set(input().split())
  b=int(input()); B=set(input().split())
  print(a.issubset(b))
