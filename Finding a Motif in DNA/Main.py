from bbio import *
ss = "GATATATGCATATACTT"
s = "ATAT"

grep = ""
frr = []

for i in range(len(ss)):
  if ss[i] == s[0]:
    grep = ss[i:i+4]
    if grep == s:
      frr.append(str(i+1))
    

print " ".join(frr)
