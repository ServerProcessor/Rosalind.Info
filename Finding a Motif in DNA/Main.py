from bbio import *
ss = "GATATATGCATATACTT"
s = "ATAT"

grep = ""
frr = []

for i in range(len(ss)):
  if ss[i] == s[0]:
    grep = ss[i:len(s)]
    if grep == s:
      frr.append(str(i+1))
    

print " ".join(frr)
