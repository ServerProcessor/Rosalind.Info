adenine = 0 // Variable for storing A count
guanine = 0 // Variable for storing G count
cytosine = 0 // Variable for storing C count
thymine = 0 // Variable for storing T count
ss = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC' // A given sequence
for word in ss:
  if w == 'A':
    adenine = adenine + 1
  if w == 'T':
    thymine = thymine + 1
  if w == 'G':
    guanine = guanine + 1
  if w == 'C':
    cytosine = cytosine + 1
print str(adenine) + " " + str(cytosine) + " " + str(guanine) + " " + str(thymine)

