ss = "GAGCCTACTAACGGGAT"
ss2 = "CATCGTAATGACGGCCT"

ww = []

for w in ss:
  ww.append(w)

pp = []

for p in ss2:
  pp.append(p)

gg = len(ss)

c = 0

for i in range(gg):
  if ww[i] != pp[i]:
    c = c + 1

print c
