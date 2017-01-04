s = 'AAAACCCGGT' # The input Sequence
ss = s[::-1] # Reverse the String
w = []
for ww in ss:
  if ww == 'A':
    w.append('T')
  if ww == 'T':
    w.append('A')
  if ww == 'G':
    w.append('C')
  if ww == 'C':
    w.append('G')
print "".join(w)
