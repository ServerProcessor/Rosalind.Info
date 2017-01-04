from bbio import *
import itertools

ss = 3

qq = 1 

for i in range(ss+1):
  if i != 0:
    qq = qq * i
    
print qq
"\n"
s = " "
strg = ""

for ii in range(ss+1):
    if ii != 0:
      strg = strg + str(ii)

comb = itertools.permutations(strg)
for x in comb: 
  print s.join(x)
  
# s = "-";
# seq = ("a", "b", "c"); # This is sequence of strings.
# print s.join( seq )

# When we run above program, it produces following result −

# a-b-c
