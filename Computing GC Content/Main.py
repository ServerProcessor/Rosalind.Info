Dname = "Rosalind_6404"
ss = "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
Dname2 = "Rosalind_5959"
ss2 = "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"
Dname3 = "Rosalind_0808"
ss3 = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

c = 0
c2 = 0
c3 = 0

for ww in ss:
  if (ww == 'C') | (ww == 'G'):
    c = c + 1

gp = 100 * (float(c) / len(ss))

for ww2 in ss2:
  if (ww2 == 'C') | (ww2 == 'G'):
    c2 = c2 + 1

gp2 = 100 * (float(c2) / len(ss2))

for ww3 in ss3:
  if (ww3 == 'C') | (ww3 == 'G'):
    c3 = c3 + 1

gp3 = 100 * (float(c3) / len(ss3))

if c > c2:
  if c > c3:
    print "" , Dname,
    print gp
  else:
    print "" , Dname3,
    print gp3
if c2 > c:
  if c2 > c3:
    print "" , Dname2,
    print gp2
  else:
    print "" , Dname3,
    print gp3

