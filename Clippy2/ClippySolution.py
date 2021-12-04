from z3 import *
mylist = [65,53,125,28,127,20,87,3,69,62,73,121,14,81,50,94,111,31,111,22,73,61,9,124,27,115,68,27,110,49,85,101,17,78,32,19,103,56,75,59,66,115,29,122,7]
print("A", end = "")
print("t", end = "")
for x in range (0,len(mylist)+1):
  if x == len(mylist)-2:
    break
  a=BitVec('x1',32)
  s=Solver()
  s.add(a^mylist[x+1]==BitVecVal(mylist[x+2],32), a>32, a<126)
  s.check()
  x = str(s.model())
  y = x.split(" ")
  solution = y[2].split("]")
  
  print(chr(int(solution[0])), end = "")
